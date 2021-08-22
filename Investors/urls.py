from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('buy', views.Buystock, name='buy-stock'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('logout', views.Logoutuser, name='logout'),
    path('checkout', views.checkout, name='checkout')
]
