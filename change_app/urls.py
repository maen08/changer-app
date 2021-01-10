
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.request_change, name='request_change'),
    
]
