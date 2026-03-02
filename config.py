# dr_r_project/settings.py
import os
import logging
from pathlib import Path

# -------------------------
# Paths
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Logging
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------
# Secret Key
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    logger.warning(
        "SECRET_KEY not set! Using fallback (not secure for production)"
    )
    SECRET_KEY = 'research-agent-2026-fallback-key-change-in-production'

# -------------------------
# Debug
# -------------------------
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() in ['true', '1', 'yes']

# -------------------------
# Allowed Hosts
# -------------------------
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# -------------------------
# Application definition
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dr_r_app',  # Your AI app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dr_r_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'dr_r_app' / 'templates'],  # Your templates folder
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

WSGI_APPLICATION = 'dr_r_project.wsgi.application'

# -------------------------
# Database (keep default SQLite for now)
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Password validation (default)
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -------------------------
# Static files
# -------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'dr_r_app' / 'static']

# -------------------------
# Security settings (similar to Flask config)
# -------------------------
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# -------------------------
# Custom app settings
# -------------------------
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
if not GROQ_API_KEY:
    logger.error("❌ GROQ_API_KEY is not set! The search agent may fail.")

MAX_RESULTS_DEFAULT = int(os.environ.get('MAX_RESULTS_DEFAULT', 20))
REQUEST_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 30))

CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')

# -------------------------
# Validation at startup (optional)
# -------------------------
if not GROQ_API_KEY:
    logger.warning("⚠️ GROQ_API_KEY missing - search agent may not work")
if 'fallback' in SECRET_KEY:
    logger.warning("⚠️ SECRET_KEY is using fallback - change for production")
