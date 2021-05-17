from django.contrib import admin
from .models import User, Product, Order, ProductCategory, Cart


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = [
        "username",
        "email",
        "is_superuser"
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


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = [
        "category_code",
        "category_name",
    ]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [
        "order_id",
        "purchase_by"
    ]


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = [
        "added_products",
        "product_count"
    ]


admin.site.register(User, UserAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
