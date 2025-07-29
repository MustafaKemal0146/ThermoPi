#!/usr/bin/env python3
"""
ThermoPi Test Script
Fan kontrolünü test etmek için basit script
"""

import time
import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("❌ RPi.GPIO kütüphanesi bulunamadı!")
    print("📦 Yüklemek için: pip3 install RPi.GPIO")
    sys.exit(1)

def test_fan_control():
    """Test fan control functionality"""
    fan_pin = 18
    pwm_frequency = 25000
    
    print("🌡️ ThermoPi Fan Test Başlatılıyor...")
    print(f"🔌 GPIO Pin: {fan_pin}")
    print(f"⚡ PWM Frekansı: {pwm_frequency} Hz")
    
    try:
        # GPIO setup
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(fan_pin, GPIO.OUT)
        pwm = GPIO.PWM(fan_pin, pwm_frequency)
        pwm.start(0)
        
        print("✅ GPIO başarıyla başlatıldı")
        print("🔊 Fan sesini dinleyin...")
        
        # Test different speeds with longer delays
        test_speeds = [0, 25, 50, 75, 100]
        
        for speed in test_speeds:
            print(f"🌀 Fan hızı: {speed}% - 3 saniye bekleniyor...")
            pwm.ChangeDutyCycle(speed)
            time.sleep(3)
        
        # Gradual decrease
        print("📉 Fan hızı yavaş yavaş azaltılıyor...")
        for speed in range(100, -1, -10):
            print(f"🌀 Fan hızı: {speed}%")
            pwm.ChangeDutyCycle(speed)
            time.sleep(1)
        
        print("✅ Test tamamlandı - Fan durduruldu")
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        print("🔧 Sudo ile çalıştırmayı deneyin: sudo python3 test_fan.py")
    
    finally:
        try:
            pwm.ChangeDutyCycle(0)  # Fan'ı kapat
            time.sleep(0.5)
            pwm.stop()
            GPIO.cleanup()
            print("🧹 GPIO temizlendi")
        except:
            pass

def read_temperature():
    """Read and display CPU temperature"""
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp_raw = f.read().strip()
            temp_celsius = float(temp_raw) / 1000.0
            print(f"🌡️ CPU Sıcaklığı: {temp_celsius:.1f}°C")
            return temp_celsius
    except Exception as e:
        print(f"❌ Sıcaklık okuma hatası: {e}")
        return 0.0

if __name__ == "__main__":
    print("🧪 ThermoPi Test Modu")
    print("=" * 40)
    
    # Read temperature first
    temp = read_temperature()
    
    # Ask user if they want to test fan
    try:
        choice = input("\n🎯 Fan kontrolünü test etmek istiyor musunuz? (e/h): ").lower()
        if choice == 'e':
            test_fan_control()
        else:
            print("👋 Test iptal edildi")
    except KeyboardInterrupt:
        print("\n👋 Çıkılıyor...")