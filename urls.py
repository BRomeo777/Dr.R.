# dr_r_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dr_r_app.urls')),  # Include app URLs
]
