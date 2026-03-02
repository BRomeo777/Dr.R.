import os
from django.core.wsgi import get_wsgi_application

# Changed from 'dr_r_project.settings' to 'settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
