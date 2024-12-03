from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Add login, logout, and profile URLs as needed
]
