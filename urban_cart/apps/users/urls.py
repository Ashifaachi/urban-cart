from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/',views.account,name='account'),
    path('logout/', views.logout, name='logout'),


]
