from django.contrib import admin
from django.urls import path
import views  # Import your views directly from the root directory

urlpatterns = [
    path('admin/', admin.site.urls),
    # Point the home page directly to the home function in your views.py
    path('', views.home, name='home'), 
    
    # If you have a specific search/chat function for the AI:
    # path('search/', views.search_view, name='search'),
]
