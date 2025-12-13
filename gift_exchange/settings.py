
# (LOGGING tanımı BASE_DIR tanımlandıktan sonra yeniden eklenecek)
"""
Django settings for gift_exchange project.
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# 1. LOCAL GELİŞTİRME İÇİN .ENV YÜKLEME
# Render'da bu dosya olmayacak, Render kendi panelinden okuyacak.
# Bilgisayarında ise .env dosyasından okuyacak.
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------
# LOGGING AYARLARI (Tüm hataları terminale ve dosyaya yaz)
# ---------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': str(BASE_DIR / 'django-error.log'),
            'level': 'ERROR',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'ERROR',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# ---------------------------------------------------------
# 🔒 GÜVENLİK AYARLARI
# ---------------------------------------------------------

# SECRET_KEY'i ortam değişkeninden al, yoksa (localde) varsayılanı kullan
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-dev')

# Render'da RENDER=true diye bir değişken otomatik vardır.
# Eğer Render'daysak DEBUG False olsun, yoksa True olsun.
DEBUG = 'RENDER' not in os.environ

# Render uygulamanızın adresi buraya gelmeli.
# '*' şimdilik kalsın ama prodüksiyonda 'senin-app.onrender.com' olması daha iyidir.
ALLOWED_HOSTS = ['*']

# Render'da form gönderirken hata almamak için:
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    # Eğer özel alan adı alırsan onu da buraya ekle örn: 'https://mysite.com'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landing', # Senin uygulaman
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise burada olmalı
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gift_exchange.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gift_exchange.wsgi.application'


# ---------------------------------------------------------
# 🗄️ VERİTABANI AYARLARI (SUPABASE & LOCAL)
# ---------------------------------------------------------

# DATABASE_URL varsa Supabase kullan, yoksa SQLite (local geliştirme için)
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True 
        )
    }
else:
    # Local bilgisayarında çalışırken burası çalışır (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# 🎨 STATİK DOSYALAR (CSS, JS, IMAGES)
# ---------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise sıkıştırması
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------------------------------------
# ---------------------------------------------------------
# 📧 EMAIL AYARLARI (SENDGRID - SMTP fallback)
# ---------------------------------------------------------
# Tercih: Anymail'in resmi SendGrid desteği artık önerilmediği için
# burada SendGrid'in SMTP arayüzünü kullanıyoruz. Render/production'da
# environment değişkenlerine `SENDGRID_API_KEY` ve `SENDGRID_FROM_EMAIL` ekle.

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = os.environ.get('SENDGRID_FROM_EMAIL', 'noreply@iucdevops.com')

if SENDGRID_API_KEY:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = 'apikey'  # SendGrid SMTP kullanıcı adı sabittir
    EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    # Geliştirme ortamı için console backend (mail terminale yazılır)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Not: SendGrid panelinde `DEFAULT_FROM_EMAIL` adresinin verify edildiğinden emin ol.