from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField()
    additional_img = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=1023, default="")

    def __str__(self):
        return f"{self.name}"


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"name: {self.name}, product: {self.product.name}"
