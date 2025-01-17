from django.db import models

# Create your models here.
# Choices for Product Category
class MainCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return f"{self.name} ({self.main_category.name})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image_url = models.URLField()
    site_link = models.URLField()
    ratings = models.FloatField(null=True, blank=True)
    no_of_ratings = models.PositiveIntegerField(null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Slider(models.Model):
    add_head = models.CharField(max_length=255, verbose_name="Heading")
    add_sub_head = models.CharField(max_length=255, verbose_name="Subheading", blank=True, null=True)
    add_text = models.TextField(verbose_name="Text Description", blank=True, null=True)
    add_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)
    add_image = models.ImageField(upload_to='slider_images/', verbose_name="Image")

    def __str__(self):
        return self.add_head