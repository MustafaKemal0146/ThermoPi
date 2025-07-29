# 🌡️ ThermoPi - Akıllı Fan Kontrol Sistemi

**🚀 Raspberry Pi 5 için gelişmiş soğutma çözümü:** [Hemen başlayın](#-kurulum)


<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&width=1000&lines=ThermoPi+-+Akıllı+Fan+Kontrol+Sistemi;Raspberry+Pi+5+Soğutma+Çözümü;Otomatik+Sıcaklık+Yönetimi;Manuel+ve+Akıllı+Kontrol+Modu" alt="Typing SVG" />
</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white)](https://raspberrypi.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6B35?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![GPIO](https://img.shields.io/badge/GPIO-PWM%20Control-green?style=for-the-badge&logo=raspberry-pi&logoColor=white)](https://pypi.org/project/RPi.GPIO/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Turkish](https://img.shields.io/badge/Language-Türkçe-red?style=for-the-badge&logo=google-translate&logoColor=white)](https://tr.wikipedia.org/wiki/T%C3%BCrk%C3%A7e)

</div>

<p align="center">
<img src="https://images.pexels.com/photos/163100/circuit-circuit-board-resistor-computer-163100.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Raspberry Pi Circuit" width="600"/>
<br/>
<em>Raspberry Pi 5 için profesyonel soğutma kontrolü</em>
<br/><br/>
<img src="https://images.pexels.com/photos/442150/pexels-photo-442150.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Temperature Control" width="600"/>
<br/>
<em>Gerçek zamanlı sıcaklık izleme ve akıllı fan kontrolü</em>
</p>

> **🔥 Akıllı Soğutma Sistemi:** ThermoPi, Raspberry Pi 5'inizin optimal sıcaklıkta çalışmasını sağlayan gelişmiş bir fan kontrol sistemidir. Hem manuel hem de otomatik kontrol modları ile mükemmel performans sunar.

## ✨ Özellikler

- 🎛️ **Çift Arayüz**: Hem grafiksel (GUI) hem de terminal tabanlı kontrol
- 🎯 **Manuel Kontrol**: Gerçek zamanlı fan hızı ayarı (slider ve terminal)
- 🤖 **Otomatik Mod**: Sıcaklık bazlı akıllı fan kontrolü
- 📊 **Canlı İzleme**: Sürekli CPU sıcaklığı okuma ve görüntüleme
- 📝 **Veri Kayıt**: Zaman damgalı sıcaklık ve fan hızı logları
- ⚡ **Thread Güvenli**: Responsive GUI ile arka plan izleme
- 🛡️ **Hata Yönetimi**: Donanım erişim hatalarına karşı koruma
- 🧪 **Simülasyon Modu**: GPIO olmadan test imkanı

## 🛠️ Teknolojiler

- **Platform**: Raspberry Pi 5 (Özel PWM fan header)
- **Dil**: Python 3.7+ (GDScript benzeri basitlik)
- **GUI Framework**: Tkinter (Cross-platform)
- **Hardware Control**: RPi.GPIO (PWM kontrol)
- **Threading**: Python threading (Responsive UI)
- **Data Format**: Text-based logging
- **Architecture**: Object-oriented modular design

## 🔧 Donanım Gereksinimleri

| Bileşen | Minimum | Önerilen |
|---------|---------|----------|
| **Raspberry Pi** | Pi 5 | Pi 5 (8GB RAM) |
| **Fan** | PWM uyumlu | Noctua/Arctic PWM fan |
| **Python** | 3.7+ | 3.11+ |
| **GPIO Pin** | Pin 18 (PWM) | Pin 18 (PWM) |
| **Power** | 5V/2A | 5V/3A+ |

## 🚀 Kurulum

### Hızlı Başlangıç

1. **Sistem güncellemesi**
```bash
sudo apt update && sudo apt upgrade -y
```

2. **Gerekli paketleri yükleyin**
```bash
# Python ve GUI kütüphaneleri
sudo apt install python3-pip python3-tk python3-dev

# GPIO kütüphanesi
pip3 install RPi.GPIO
```

3. **Projeyi indirin**
```bash
git clone https://github.com/yourusername/ThermoPi.git
cd ThermoPi
```

4. **Çalıştırma izni verin**
```bash
chmod +x rpi_fan_controller.py
```

5. **Uygulamayı başlatın**
```bash
python3 rpi_fan_controller.py
```

### Otomatik Başlatma (Opsiyonel)

```bash
# Systemd servisi oluştur
sudo nano /etc/systemd/system/thermopi.service

# Servisi etkinleştir
sudo systemctl enable thermopi.service
sudo systemctl start thermopi.service
```

## 🎮 Kullanım

### 🖥️ Arayüz Seçimi

Program başlatıldığında size iki seçenek sunulur:

```
Raspberry Pi 5 Fan Controller
Choose interface:
1. GUI (Tkinter)     # 🎨 Grafiksel arayüz
2. Terminal          # ⌨️ Terminal arayüzü
```

### 🎨 GUI Arayüzü

#### 🌟 Ana Özellikler
- **🌡️ Sıcaklık Göstergesi**: Gerçek zamanlı CPU sıcaklığı
- **🔄 Mod Değiştirici**: Manuel/Otomatik arası geçiş
- **🎛️ Hız Slider'ı**: 0-100% fan hızı kontrolü
- **📊 Durum Göstergesi**: Anlık fan hızı ve mod bilgisi

#### 🎯 Kontrol Modları

##### 🎛️ Manuel Mod
- Kullanıcı fan hızını doğrudan kontrol eder
- Slider ile 0-100% arası ayar
- Gerçek zamanlı PWM güncellemesi
- Otomatik kontrol devre dışı

##### 🤖 Otomatik Mod  
- Sıcaklık bazlı akıllı kontrol
- **50°C altı**: Fan kapalı (0%)
- **50-65°C arası**: Doğrusal artış (20-80%)
- **65°C üstü**: Maksimum hız (100%)

### ⌨️ Terminal Arayüzü

#### 📋 Menü Seçenekleri
```
--- Raspberry Pi 5 Fan Controller ---
CPU Temperature: 45.2°C
Fan Speed: 0%
Control Mode: Manual
----------------------------------------

Options:
1. Toggle control mode (Manual/Automatic)
2. Set fan speed (Manual mode only)  
3. View current status
4. Exit
```

#### 🎯 Klavye Kısayolları
- **1**: Mod değiştir (Manuel ↔ Otomatik)
- **2**: Fan hızı ayarla (Manuel modda)
- **3**: Durum görüntüle
- **4**: Çıkış
- **Ctrl+C**: Acil çıkış

## 📊 Sıcaklık Algoritması

### 🧮 Otomatik Kontrol Formülü

```python
def calculate_auto_speed(temperature):
    if temperature < 50.0:
        return 0  # Fan kapalı
    elif temperature > 65.0:
        return 100  # Maksimum hız
    else:
        # Doğrusal interpolasyon
        temp_range = 65.0 - 50.0  # 15°C
        speed_range = 80 - 20     # 60%
        ratio = (temperature - 50.0) / temp_range
        speed = 20 + (speed_range * ratio)
        return int(speed)
```

### 📈 Sıcaklık Eşikleri

| Sıcaklık | Fan Hızı | Açıklama |
|-----------|----------|----------|
| < 50°C | 0% | Sessiz çalışma |
| 50-55°C | 20-40% | Hafif soğutma |
| 55-60°C | 40-60% | Orta soğutma |
| 60-65°C | 60-80% | Yoğun soğutma |
| > 65°C | 100% | Maksimum soğutma |

## 🔧 Konfigürasyon

### ⚙️ Sıcaklık Eşiklerini Değiştirme

`FanController` sınıfında:

```python
class FanController:
    def __init__(self):
        # Sıcaklık eşikleri (°C)
        self.temp_min = 50.0    # Fan başlama sıcaklığı
        self.temp_max = 65.0    # Maksimum hız sıcaklığı
        
        # Hız aralıkları (%)
        self.speed_min = 20     # Minimum aktif hız
        self.speed_max = 80     # Maksimum normal hız
```

### 🔌 PWM Ayarları

```python
# GPIO pin (BCM modu)
fan_pin = 18

# PWM frekansı (Hz)
pwm_frequency = 25000  # 25kHz (sessiz çalışma)
```

### 📝 Log Ayarları

```python
# Log dosyası
log_file = "fan_control_log.txt"

# Log formatı
log_format = "%(asctime)s - Temp: %(temp).1f°C, Fan: %(speed)d%%, Mode: %(mode)s"
```

## 📁 Proje Yapısı

```
ThermoPi/
├── rpi_fan_controller.py    # Ana uygulama
├── requirements.txt         # Python bağımlılıkları
├── README.md               # Bu dokümantasyon
├── fan_control_log.txt     # Otomatik oluşturulan log
├── LICENSE                 # MIT lisansı
└── assets/                 # Gelecekteki kaynaklar
    ├── icons/
    ├── sounds/
    └── themes/
```

## 🏗️ Sınıf Mimarisi

### 🎛️ FanController
**Donanım kontrol sınıfı:**
- GPIO başlatma ve PWM kontrolü
- Thermal zone'dan sıcaklık okuma
- Otomatik hız hesaplama
- Donanım temizleme

### 📝 DataLogger  
**Veri kayıt sınıfı:**
- Dosya tabanlı log kayıtları
- Zaman damgalı girişler
- Hata yönetimi

### 🖥️ FanControlGUI
**Tkinter tabanlı GUI:**
- Gerçek zamanlı görüntü güncellemeleri
- İnteraktif kontroller
- Arka plan izleme thread'i

### ⌨️ TerminalInterface
**Komut satırı arayüzü:**
- Menü tabanlı etkileşim
- Durum gösterimi
- Arka plan izleme

## 🛡️ Hata Yönetimi

### 🔧 Donanım Hataları
- **GPIO başlatma hatası**: Simülasyon moduna geçiş
- **PWM kontrol hatası**: Konsol uyarısı
- **Sıcaklık okuma hatası**: Simüle edilmiş değer

### 📁 Dosya Hataları
- **Log yazma hatası**: Konsol çıktısına devam
- **İzin hatası**: Sudo önerisi
- **Disk dolu**: Uyarı mesajı

### 🧵 Thread Güvenliği
- **GUI donması**: Arka plan thread'i ile önleme
- **Kaynak sızıntısı**: Proper cleanup
- **Çoklu erişim**: Thread-safe operasyonlar

## 🧪 Test Modu

### 🖥️ Simülasyon Özellikleri
```python
# GPIO olmadan çalışma
if GPIO is None:
    print("Simulation mode active")
    
# Simüle edilmiş sıcaklık
def get_simulated_temp():
    return 45.0 + (time.time() % 30)  # 45-75°C arası
```

### 🔍 Debug Modu
```bash
# Verbose çıktı ile çalıştırma
python3 rpi_fan_controller.py --debug

# Log seviyesi ayarlama
export THERMOPI_LOG_LEVEL=DEBUG
```

## 🚨 Sorun Giderme

### 🔐 İzin Sorunları
```bash
# GPIO erişim izni
sudo usermod -a -G gpio $USER
sudo reboot

# Veya sudo ile çalıştırma
sudo python3 rpi_fan_controller.py
```

### 📦 Eksik Bağımlılıklar
```bash
# Tüm bağımlılıkları yükle
pip3 install -r requirements.txt

# Manuel yükleme
sudo apt install python3-rpi.gpio python3-tk
```

### 🌀 Fan Çalışmıyor
- ✅ Fan bağlantısını kontrol edin (GPIO 18)
- ✅ PWM uyumluluğunu doğrulayın
- ✅ Güç kaynağını kontrol edin (5V/3A+)
- ✅ Fan voltajını ölçün (multimetre)

### 🌡️ Sıcaklık Okunamıyor
```bash
# Thermal zone kontrolü
cat /sys/class/thermal/thermal_zone0/temp

# Çıktı: 45123 (45.123°C)
```

## 🎯 Gelecek Planları

- [ ] 🎵 **Ses Efektleri**: Fan durumu için ses geri bildirimi
- [ ] 📱 **Web Arayüzü**: Tarayıcı tabanlı kontrol paneli
- [ ] 📊 **Grafik Gösterim**: Sıcaklık ve fan hızı grafikleri
- [ ] 🌐 **IoT Entegrasyonu**: MQTT/HTTP API desteği
- [ ] 🎮 **Gamepad Desteği**: Fiziksel kontrol cihazları
- [ ] 🔔 **Bildirimler**: E-posta/SMS uyarı sistemi
- [ ] 🎨 **Tema Desteği**: Karanlık/aydınlık mod
- [ ] 📈 **Makine Öğrenmesi**: Adaptif soğutma algoritması

## 🤝 Katkıda Bulunma

### 🔧 Geliştirme Süreci
1. Bu projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

### 📝 Katkı Alanları
- **🐛 Bug Raporları**: Hata bildirimleri
- **💡 Özellik Önerileri**: Yeni fonksiyon fikirleri
- **📚 Dokümantasyon**: README ve kod yorumları
- **🌐 Çeviriler**: Diğer dillere çeviri
- **🎨 UI/UX**: Arayüz iyileştirmeleri
- **⚡ Performans**: Optimizasyon önerileri

## 📚 Kaynaklar

### 🔗 Teknik Dokümantasyon
- [Raspberry Pi 5 GPIO Pinout](https://pinout.xyz/)
- [RPi.GPIO Documentation](https://pypi.org/project/RPi.GPIO/)
- [Python Tkinter Guide](https://docs.python.org/3/library/tkinter.html)
- [PWM Fan Control Theory](https://en.wikipedia.org/wiki/Pulse-width_modulation)

### 🛠️ Geliştirme Araçları
- [Python 3.11+](https://python.org/)
- [Raspberry Pi OS](https://raspberrypi.org/software/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git Version Control](https://git-scm.com/)

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT License - Özgürce kullanın, değiştirin, dağıtın
```

## 👨‍💻 Geliştirici

<div align="center">
<img src="https://images.pexels.com/photos/163100/circuit-circuit-board-resistor-computer-163100.jpeg?auto=compress&cs=tinysrgb&w=150&h=150&fit=crop" width="100" style="border-radius: 50%;" alt="ThermoPi Developer"/>

**ThermoPi Development Team**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![Website](https://img.shields.io/badge/Website-00FF88?style=for-the-badge&logo=google-chrome&logoColor=white)](https://yourwebsite.com)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your@email.com)

</div>

## ⭐ Destek

Eğer ThermoPi Raspberry Pi'nizin soğutma performansını artırdıysa, lütfen ⭐ vererek destekleyin!

### 📊 İstatistikler

<div align="center">
<img src="https://komarev.com/ghpvc/?username=ThermoPi&color=00ff88&style=for-the-badge&label=Project+Views" />
</div>

---

<div align="center">

**Made with 🔥 for optimal Raspberry Pi cooling**

*"Mükemmel sıcaklık kontrolü, mükemmel performans"*

</div>

<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&duration=4000&pause=1000&color=00FF88&center=true&vCenter=true&width=600&lines=Thank+you+for+using+ThermoPi;Keep+your+Pi+cool+and+efficient;Every+degree+matters+for+performance" alt="Footer Typing SVG" />
</div>
