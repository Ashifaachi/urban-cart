from django.db import models

# Create your models here.
# Choices for Product Category
CATEGORY_CHOICES = [
    ('casual', 'Casual Shoes'),
    ('formal', 'Formal Shoes'),
    ('sports', 'Sports Shoes'),
    ('kids', 'Kids Shoes'),
]

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.PositiveIntegerField()
    product_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    product_image1 = models.ImageField(upload_to='products/')
    product_image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    product_image3 = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product_name
    
class Slider(models.Model):
    add_head = models.CharField(max_length=255, verbose_name="Heading")
    add_sub_head = models.CharField(max_length=255, verbose_name="Subheading", blank=True, null=True)
    add_text = models.TextField(verbose_name="Text Description", blank=True, null=True)
    add_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)
    add_image = models.ImageField(upload_to='slider_images/', verbose_name="Image")

    def __str__(self):
        return self.add_head