import os
from pathlib import Path

# 1. FIX: Since you have no folders, the base directory is just 'parent'
BASE_DIR = Path(__file__).resolve().parent

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key-change-me")

# Keep DEBUG True for now so you can see any final errors in the browser
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # REMOVED "dr_r_app" because the folder does not exist
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# 2. FIX: Look for 'urls.py' in the root folder
ROOT_URLCONF = "urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], # In case you have a templates folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 3. FIX: Look for 'wsgi.py' in the root folder
WSGI_APPLICATION = "wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 4. Groq API Key for your Gastric Cancer AI
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
