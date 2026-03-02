from django.contrib import admin
from django.urls import path
import views  # This looks for views.py in your root directory

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. The Main Page (Your AI interface)
    path('', views.index, name='index'), 
    
    # 2. The Search Endpoint (Where the Llama model processes queries)
    path('search', views.search, name='search'),
    
    # 3. Health Check (To see if the Groq API is connected)
    path('health', views.health, name='health'),
]
