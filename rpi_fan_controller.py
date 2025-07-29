#!/usr/bin/env python3
"""
Raspberry Pi 5 Fan Controller
A comprehensive fan control system with GUI and terminal interfaces
Supports both manual and automatic temperature-based fan control
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import logging
import sys
import os
from datetime import datetime
from typing import Optional, Callable

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Warning: RPi.GPIO not available. Running in simulation mode.")
    GPIO = None

class FanController:
    """Core fan controller class handling hardware PWM and temperature reading"""
    
    def __init__(self, fan_pin: int = 18, pwm_frequency: int = 25000):
        self.fan_pin = fan_pin
        self.pwm_frequency = pwm_frequency
        self.pwm = None
        self.current_speed = 0
        self.is_initialized = False
        
        # Temperature thresholds for automatic mode
        self.temp_min = 50.0  # Below this: fan off
        self.temp_max = 65.0  # Above this: fan at 100%
        self.speed_min = 20   # Minimum speed when fan starts
        self.speed_max = 80   # Maximum speed before 100%
        
        self.initialize_gpio()
    
    def initialize_gpio(self):
        """Initialize GPIO and PWM for fan control"""
        if GPIO is None:
            print("GPIO not available - running in simulation mode")
            self.is_initialized = True
            return
            
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.fan_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(self.fan_pin, self.pwm_frequency)
            self.pwm.start(0)
            self.is_initialized = True
            print(f"Fan controller initialized on GPIO pin {self.fan_pin}")
        except Exception as e:
            print(f"Error initializing GPIO: {e}")
            self.is_initialized = False
    
    def set_fan_speed(self, speed_percent: int):
        """Set fan speed as percentage (0-100)"""
        speed_percent = max(0, min(100, speed_percent))
        self.current_speed = speed_percent
        
        if self.pwm and self.is_initialized:
            try:
                self.pwm.ChangeDutyCycle(speed_percent)
            except Exception as e:
                print(f"Error setting fan speed: {e}")
        else:
            print(f"Simulation: Fan speed set to {speed_percent}%")
    
    def get_cpu_temperature(self) -> float:
        """Read CPU temperature from thermal zone"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                temp_raw = f.read().strip()
                temp_celsius = float(temp_raw) / 1000.0
                return temp_celsius
        except Exception as e:
            print(f"Error reading temperature: {e}")
            # Return simulated temperature for testing
            return 45.0 + (time.time() % 30)  # Simulated temp between 45-75°C
    
    def calculate_auto_speed(self, temperature: float) -> int:
        """Calculate fan speed based on temperature for automatic mode"""
        if temperature < self.temp_min:
            return 0
        elif temperature > self.temp_max:
            return 100
        else:
            # Linear interpolation between temp_min and temp_max
            temp_range = self.temp_max - self.temp_min
            speed_range = self.speed_max - self.speed_min
            temp_ratio = (temperature - self.temp_min) / temp_range
            speed = self.speed_min + (speed_range * temp_ratio)
            return int(speed)
    
    def cleanup(self):
        """Clean up GPIO resources"""
        if self.pwm:
            self.pwm.stop()
        if GPIO and self.is_initialized:
            GPIO.cleanup()
        print("GPIO cleanup completed")


class DataLogger:
    """Handle logging of temperature and fan speed data"""
    
    def __init__(self, log_file: str = "fan_control_log.txt"):
        self.log_file = log_file
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def log_data(self, temperature: float, fan_speed: int, mode: str):
        """Log temperature and fan speed data"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Temp: {temperature:.1f}°C, Fan: {fan_speed}%, Mode: {mode}"
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(log_entry + "\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")


class FanControlGUI:
    """GUI interface using Tkinter"""
    
    def __init__(self, fan_controller: FanController, data_logger: DataLogger):
        self.fan_controller = fan_controller
        self.data_logger = data_logger
        self.is_auto_mode = False
        self.is_running = True
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Raspberry Pi 5 Fan Controller")
        self.root.geometry("500x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.setup_gui()
        self.start_background_thread()
    
    def setup_gui(self):
        """Setup the GUI components"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Temperature display
        temp_frame = ttk.LabelFrame(main_frame, text="Temperature", padding="10")
        temp_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.temp_label = ttk.Label(temp_frame, text="CPU Temperature: --°C", font=("Arial", 14))
        self.temp_label.grid(row=0, column=0)
        
        # Mode control
        mode_frame = ttk.LabelFrame(main_frame, text="Control Mode", padding="10")
        mode_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.mode_var = tk.BooleanVar()
        self.mode_checkbox = ttk.Checkbutton(
            mode_frame, 
            text="Automatic Mode", 
            variable=self.mode_var,
            command=self.toggle_mode
        )
        self.mode_checkbox.grid(row=0, column=0)
        
        # Manual control
        manual_frame = ttk.LabelFrame(main_frame, text="Manual Control", padding="10")
        manual_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(manual_frame, text="Fan Speed:").grid(row=0, column=0, sticky=tk.W)
        
        self.speed_var = tk.IntVar()
        self.speed_scale = ttk.Scale(
            manual_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            command=self.on_speed_change
        )
        self.speed_scale.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.speed_label = ttk.Label(manual_frame, text="0%")
        self.speed_label.grid(row=1, column=2, padx=10)
        
        # Status display
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Current Fan Speed: 0%", font=("Arial", 12))
        self.status_label.grid(row=0, column=0)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        manual_frame.columnconfigure(0, weight=1)
    
    def toggle_mode(self):
        """Toggle between manual and automatic mode"""
        self.is_auto_mode = self.mode_var.get()
        
        if self.is_auto_mode:
            self.speed_scale.configure(state='disabled')
            print("Switched to automatic mode")
        else:
            self.speed_scale.configure(state='normal')
            print("Switched to manual mode")
    
    def on_speed_change(self, value):
        """Handle manual speed slider change"""
        if not self.is_auto_mode:
            speed = int(float(value))
            self.fan_controller.set_fan_speed(speed)
            self.speed_label.config(text=f"{speed}%")
    
    def update_display(self, temperature: float, fan_speed: int):
        """Update GUI display with current values"""
        self.temp_label.config(text=f"CPU Temperature: {temperature:.1f}°C")
        self.status_label.config(text=f"Current Fan Speed: {fan_speed}%")
        
        if not self.is_auto_mode:
            self.speed_var.set(fan_speed)
            self.speed_label.config(text=f"{fan_speed}%")
    
    def background_worker(self):
        """Background thread for temperature monitoring and fan control"""
        while self.is_running:
            try:
                temperature = self.fan_controller.get_cpu_temperature()
                
                if self.is_auto_mode:
                    # Automatic mode: calculate speed based on temperature
                    target_speed = self.fan_controller.calculate_auto_speed(temperature)
                    self.fan_controller.set_fan_speed(target_speed)
                else:
                    # Manual mode: use current slider value
                    target_speed = self.fan_controller.current_speed
                
                # Update GUI in main thread
                self.root.after(0, self.update_display, temperature, self.fan_controller.current_speed)
                
                # Log data
                mode = "Auto" if self.is_auto_mode else "Manual"
                self.data_logger.log_data(temperature, self.fan_controller.current_speed, mode)
                
                time.sleep(1)  # Update every second
                
            except Exception as e:
                print(f"Error in background worker: {e}")
                time.sleep(1)
    
    def start_background_thread(self):
        """Start the background monitoring thread"""
        self.worker_thread = threading.Thread(target=self.background_worker, daemon=True)
        self.worker_thread.start()
    
    def on_closing(self):
        """Handle window closing"""
        self.is_running = False
        self.fan_controller.cleanup()
        self.root.destroy()
    
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()


class TerminalInterface:
    """Terminal-based interface for fan control"""
    
    def __init__(self, fan_controller: FanController, data_logger: DataLogger):
        self.fan_controller = fan_controller
        self.data_logger = data_logger
        self.is_auto_mode = False
        self.is_running = True
    
    def display_status(self):
        """Display current status"""
        temperature = self.fan_controller.get_cpu_temperature()
        fan_speed = self.fan_controller.current_speed
        mode = "Automatic" if self.is_auto_mode else "Manual"
        
        print(f"\n--- Raspberry Pi 5 Fan Controller ---")
        print(f"CPU Temperature: {temperature:.1f}°C")
        print(f"Fan Speed: {fan_speed}%")
        print(f"Control Mode: {mode}")
        print("-" * 40)
    
    def show_menu(self):
        """Display menu options"""
        print("\nOptions:")
        print("1. Toggle control mode (Manual/Automatic)")
        print("2. Set fan speed (Manual mode only)")
        print("3. View current status")
        print("4. Exit")
        print("Choice: ", end="")
    
    def handle_input(self, choice: str):
        """Handle user input"""
        if choice == "1":
            self.is_auto_mode = not self.is_auto_mode
            mode = "Automatic" if self.is_auto_mode else "Manual"
            print(f"Switched to {mode} mode")
            
        elif choice == "2":
            if self.is_auto_mode:
                print("Cannot set manual speed in automatic mode")
            else:
                try:
                    speed = int(input("Enter fan speed (0-100%): "))
                    speed = max(0, min(100, speed))
                    self.fan_controller.set_fan_speed(speed)
                    print(f"Fan speed set to {speed}%")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 100")
                    
        elif choice == "3":
            self.display_status()
            
        elif choice == "4":
            self.is_running = False
            print("Exiting...")
            
        else:
            print("Invalid choice. Please try again.")
    
    def run_monitoring_loop(self):
        """Run the monitoring loop in background"""
        while self.is_running:
            try:
                temperature = self.fan_controller.get_cpu_temperature()
                
                if self.is_auto_mode:
                    target_speed = self.fan_controller.calculate_auto_speed(temperature)
                    self.fan_controller.set_fan_speed(target_speed)
                
                # Log data
                mode = "Auto" if self.is_auto_mode else "Manual"
                self.data_logger.log_data(temperature, self.fan_controller.current_speed, mode)
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(1)
    
    def run(self):
        """Run the terminal interface"""
        # Start monitoring in background thread
        monitor_thread = threading.Thread(target=self.run_monitoring_loop, daemon=True)
        monitor_thread.start()
        
        print("Raspberry Pi 5 Fan Controller - Terminal Mode")
        self.display_status()
        
        try:
            while self.is_running:
                self.show_menu()
                choice = input().strip()
                self.handle_input(choice)
                
        except KeyboardInterrupt:
            print("\nExiting...")
            self.is_running = False
        
        finally:
            self.fan_controller.cleanup()


def main():
    """Main function to run the application"""
    print("Raspberry Pi 5 Fan Controller")
    print("Choose interface:")
    print("1. GUI (Tkinter)")
    print("2. Terminal")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
    except KeyboardInterrupt:
        print("\nExiting...")
        return
    
    # Initialize components
    fan_controller = FanController()
    data_logger = DataLogger()
    
    if choice == "1":
        # Run GUI interface
        try:
            gui = FanControlGUI(fan_controller, data_logger)
            gui.run()
        except Exception as e:
            print(f"Error running GUI: {e}")
            fan_controller.cleanup()
    
    elif choice == "2":
        # Run terminal interface
        try:
            terminal = TerminalInterface(fan_controller, data_logger)
            terminal.run()
        except Exception as e:
            print(f"Error running terminal interface: {e}")
            fan_controller.cleanup()
    
    else:
        print("Invalid choice. Exiting...")
        fan_controller.cleanup()


if __name__ == "__main__":
    main()