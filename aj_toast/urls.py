
from django.urls import path
from .views import ToastConfig

urlpatterns = [
    path('', ToastConfig, name='toast'),
  
]
