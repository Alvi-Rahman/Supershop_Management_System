from django.contrib import admin
from .models import User, Product, Order
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = [
        "username",
        "password",
        "email"
    ]
    list_filter = [
        "username",
        "email"
    ]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
        "product_code",
        "product_name",
        "product_category",
        "product_unit_price",
        "current_stock"
    ]
    list_filter = [
        "product_name"
    ]


class OrderAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
        "order_id",
        "purchased_products",
        "purchase_by"
    ]