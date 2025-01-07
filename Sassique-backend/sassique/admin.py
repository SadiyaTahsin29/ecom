from django.contrib import admin
from .models import User, Category, Product, Order, OrderItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for User model.
    """
    list_display = ("username", "email", "is_verified",
                    "is_staff", "is_active")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_verified", "is_active")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model.
    """
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for Product model.
    """
    list_display = ("name", "category", "price", "stock", "availability")
    search_fields = ("name", "category__name")
    list_filter = ("availability", "category")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for Order model.
    """
    list_display = ("id", "user", "status", "created_at", "total_price")
    search_fields = ("user__username",)
    list_filter = ("status", "created_at")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for OrderItem model.
    """
    list_display = ("order", "product", "quantity")
    search_fields = ("order__id", "product__name")
