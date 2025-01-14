from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('product_details/<int:product_id>/',views.product_details,name='product_details'),
     path('product_category/<str:category>/',views.product_category,name='product_category'),
     path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]
