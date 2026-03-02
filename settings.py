import os
from pathlib import Path

# 1. BASE DIRECTORY
# Since settings.py is in the root, we only need one .parent
BASE_DIR = Path(__file__).resolve().parent

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key-change-me")

# Keep DEBUG True for now so you can see errors in the browser if they happen
DEBUG = True

ALLOWED_HOSTS = ["*"]

# 2. INSTALLED APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # We do not list dr_r_app here because you have no app folder
]

# 3. MIDDLEWARE (Added WhiteNoise to prevent Internal Server Errors)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # This handles static files on Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 4. URLS AND WSGI
ROOT_URLCONF = "urls"
WSGI_APPLICATION = "wsgi.application"

# 5. TEMPLATES (Telling Django exactly where your folder is)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')], 
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

# 6. DATABASE (Using SQLite for your PhD project)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 7. STATIC FILES (Required for Render)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This allows WhiteNoise to compress files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 8. AI SETTINGS
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
