
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.request_change, name='request_change'),
    path('hist/', views.history_view, name='hist'),
    path('provider/', views.change_provider_view, name='provider'),
]


