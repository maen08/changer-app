from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserLoginView.as_view(), name='register'),
    path('logout/', views.UserLoginView.as_view(), name='logout'),
]