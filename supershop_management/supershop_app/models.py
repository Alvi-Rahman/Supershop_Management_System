from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.username


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_code = models.UUIDField(default=uuid.uuid4)
    category_name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.UUIDField(default=uuid.uuid4)
    product_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_unit_price = models.FloatField(default=0.0)
    current_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.UUIDField(default=uuid.uuid4)
    purchased_products = models.ManyToManyField(Product)
    purchase_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    order_placed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)


