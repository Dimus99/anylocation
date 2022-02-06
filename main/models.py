from django.db import models
from django.contrib import admin


# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField()
    additional_img = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=1023, default="")
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)

    def productvariant_set1(self):
        return [str(i.name) for i in self.productvariant_set.all()]

    def __str__(self):
        return f"{self.name}"


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"name: {self.name}, product: {self.product.name}"


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 0


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name", "description", "productvariant_set1")

    inlines = [ProductVariantInline]
