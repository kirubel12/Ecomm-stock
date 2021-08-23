from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='comp-home'),
    path('registerComp', views.Register, name='register-comp'),
    path('loginComp', views.LoginCompany, name='login-comp'),
    path('dashboardComp', views.Dashboard, name='dashboard-comp'),
    path('post', views.Post, name='post'),
    path('update/<int:stock_id>', views.UpdateStock, name='update')


]