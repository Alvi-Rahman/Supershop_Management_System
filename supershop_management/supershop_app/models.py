from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=False, null=False, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=15, null=True, blank=True)

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
    current_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    cart_code = models.UUIDField(default=uuid.uuid4)
    added_products = models.ForeignKey(Product, on_delete=models.SET_NULL, db_constraint=False, null=True)
    product_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.cart_code)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.UUIDField(default=uuid.uuid4)
    purchased_products = models.ManyToManyField(Cart, db_constraint=False)
    purchase_by = models.ForeignKey(User, on_delete=models.SET_NULL, db_constraint=False, null=True)
    order_placed = models.BooleanField(default=False)
    vat_price = models.FloatField(default=0)  # Can create a seperate model for it
    total_amount = models.FloatField(default=0)  # For Cross Matching and Ease
    invoice_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.order_id)
