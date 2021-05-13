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
        "product_category"
    ]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [
        "order_id",
        "purchase_by"
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
