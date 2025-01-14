from django.contrib import admin
from .models import Product,Slider

# Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'product_price', 'product_stock', 'product_category']
admin.site.register(Product),
admin.site.register(Slider),
