from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('register_view/', views.register_view, name='register_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout')
    ]