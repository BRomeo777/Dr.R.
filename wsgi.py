import os
from django.core.wsgi import get_wsgi_application

# IMPORTANT: Remove the "dr_r_project." part here too
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') 

application = get_wsgi_application()
