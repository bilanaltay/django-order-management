# E-Ticaret Sipariş Sistemi

Bu proje, Django ve Celery kullanarak bir sipariş işleme ve takip sistemi sunar. Kullanıcılar yeni siparişler oluşturabilir, sipariş durumlarını takip edebilir ve tüm siparişleri listeleyebilirler.

## Özellikler

- Kullanıcılar `/orders/create/` sayfasından yeni sipariş oluşturabilir.
- Sipariş oluşturulduğunda bir Celery task'i tetiklenir ve sipariş 10 saniye boyunca işlenir (simülasyon amaçlı).
- Kullanıcılar `/orders/status/` sayfasından siparişlerinin durumunu takip edebilir.
- `/orders/list/` sayfasında tüm siparişler listelenebilir.
- Siparişler duruma göre filtrelenebilir (Beklemede, İşleniyor, Tamamlandı).
- Sayfa her 5 saniyede bir otomatik olarak yenilenir.

## Gereksinimler

- Python 3.13.1
- Django
- Celery
- RabbitMQ

## Kurulum

### 1. Sanal Ortam Kurulumu
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2. Gerekli Paketlerin Yüklenmesi
```bash
pip install -r requirements.txt
```

### 3. Veritabanı Migrasyonları
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Celery ve RabbitMQ Başlatma
RabbitMQ'yu başlatın:
```bash
sudo systemctl start rabbitmq-server # macOS/Linux
rabbitmq-server start # Windows
```

Celery'i başlatın:
```bash
celery -A config worker -l info -P solo  # Windows
celery -A config worker -l info  # Linux/Mac
```

### 5. Uygulamanın Çalıştırılması
```bash
python manage.py runserver
```
