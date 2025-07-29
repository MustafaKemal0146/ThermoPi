# Raspberry Pi 5 Fan Controller

A comprehensive Python application for controlling the Raspberry Pi 5 cooling fan with both GUI and terminal interfaces. Features automatic temperature-based control and manual speed adjustment with real-time monitoring and data logging.

## Features

- **Dual Interface**: Both GUI (Tkinter) and terminal-based interfaces
- **Manual Control**: Real-time fan speed adjustment via slider or terminal input
- **Automatic Control**: Temperature-based fan speed control with configurable thresholds
- **Real-time Monitoring**: Continuous CPU temperature reading and display
- **Data Logging**: Timestamped logging of temperature and fan speed data
- **Thread-safe**: Responsive GUI with background monitoring
- **Error Handling**: Graceful handling of hardware access errors
- **Simulation Mode**: Runs without GPIO hardware for testing

## Hardware Requirements

- Raspberry Pi 5
- Fan connected to the dedicated PWM fan header (GPIO pin 18)
- Python 3.7+ with RPi.GPIO library

## Installation

1. Clone or download this repository to your Raspberry Pi 5
2. Install required dependencies:
```bash
sudo apt update
sudo apt install python3-pip python3-tk
pip3 install RPi.GPIO
```

3. Make the script executable:
```bash
chmod +x rpi_fan_controller.py
```

## Usage

### Running the Application

```bash
python3 rpi_fan_controller.py
```

You'll be prompted to choose between:
1. **GUI Interface** - Graphical interface with sliders and buttons
2. **Terminal Interface** - Text-based menu system

### GUI Interface

The GUI provides:
- **Temperature Display**: Real-time CPU temperature
- **Mode Toggle**: Switch between Manual and Automatic control
- **Speed Slider**: Manual fan speed control (0-100%)
- **Status Display**: Current fan speed and mode

### Terminal Interface

The terminal interface offers:
- Real-time status display
- Mode switching between Manual/Automatic
- Manual speed input
- Continuous background monitoring

### Control Modes

#### Manual Mode
- User controls fan speed directly via slider (GUI) or input (terminal)
- Speed range: 0% (off) to 100% (full speed)
- Real-time PWM adjustment

#### Automatic Mode
- Fan speed automatically adjusts based on CPU temperature:
  - **Below 50°C**: Fan off (0%)
  - **50°C - 65°C**: Linear increase from 20% to 80%
  - **Above 65°C**: Full speed (100%)

## Configuration

### Temperature Thresholds

You can modify the temperature thresholds in the `FanController` class:

```python
self.temp_min = 50.0  # Temperature to start fan
self.temp_max = 65.0  # Temperature for full speed
self.speed_min = 20   # Minimum fan speed when active
self.speed_max = 80   # Maximum speed before 100%
```

### PWM Settings

Default PWM settings can be adjusted:

```python
fan_pin = 18          # GPIO pin (BCM mode)
pwm_frequency = 25000 # PWM frequency in Hz
```

## Data Logging

The application automatically logs temperature and fan speed data to `fan_control_log.txt` with timestamps. Log entries include:
- Timestamp
- CPU temperature
- Fan speed percentage
- Control mode (Manual/Auto)

## File Structure

```
rpi-fan-controller/
├── rpi_fan_controller.py    # Main application
├── README.md               # This documentation
├── fan_control_log.txt     # Generated log file
└── .gitattributes         # Git configuration
```

## Classes Overview

### FanController
Core hardware control class handling:
- GPIO initialization and PWM control
- Temperature reading from thermal zone
- Automatic speed calculation
- Hardware cleanup

### DataLogger
Logging functionality:
- File-based data logging
- Timestamped entries
- Error handling for file operations

### FanControlGUI
Tkinter-based graphical interface:
- Real-time display updates
- Interactive controls
- Background monitoring thread

### TerminalInterface
Command-line interface:
- Menu-driven interaction
- Status display
- Background monitoring

## Error Handling

The application includes comprehensive error handling:
- GPIO initialization failures
- Temperature reading errors
- File I/O exceptions
- Hardware access issues
- Graceful cleanup on exit

## Simulation Mode

If RPi.GPIO is not available, the application runs in simulation mode:
- Simulated temperature readings
- Console output instead of hardware control
- Full functionality testing without hardware

## Troubleshooting

### Permission Issues
If you encounter GPIO permission errors:
```bash
sudo python3 rpi_fan_controller.py
```

### Missing Dependencies
Install missing packages:
```bash
sudo apt install python3-rpi.gpio python3-tk
```

### Fan Not Responding
- Verify fan connection to GPIO pin 18
- Check fan compatibility with PWM control
- Ensure sufficient power supply

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.
