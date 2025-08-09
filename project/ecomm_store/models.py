from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
    ]
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    category_type = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='men')

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"

    class Meta:
        verbose_name_plural = "Category"

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.IntegerField(null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')  # Upload images to 'slider/' directory
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to a Product

    def __str__(self):
        return f"Slider for {self.product.name}"
    
    class Meta:
        verbose_name_plural = "Slider"
