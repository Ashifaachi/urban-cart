from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('add_account/', views.add_account, name='add_account'),
    path('payment_status/', views.payment_status, name='payment_status'),

]
