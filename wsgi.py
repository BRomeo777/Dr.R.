import os
from django.core.wsgi import get_wsgi_application

# We remove 'dr_r_project.' because the file is just named 'settings.py'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
