import os
from pathlib import Path

# 1. FIX: Since you have no folders, the base directory is just 'parent'
BASE_DIR = Path(__file__).resolve().parent

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key-change-me")

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
    "dr_r_app", # This is your AI app
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

# 2. FIX: Look for 'urls.py' in the root, not 'dr_r_project.urls'
ROOT_URLCONF = "urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# 3. FIX: Change this to look for 'wsgi.py' in the root
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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 4. ADD: Groq API Key for your Gastric Cancer AI
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
