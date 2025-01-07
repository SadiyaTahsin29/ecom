from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.text import slugify
from django.conf import settings
from decimal import Decimal


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Includes email verification, status tracking, and resolves
    conflicts with groups and permissions fields.
    """
    email_verification_token = models.CharField(
        max_length=255, null=True, blank=True, db_index=True,
        help_text="Token for verifying the user's email address.")
    is_verified = models.BooleanField(
        default=False, db_index=True, help_text="Indicates if the user's email is verified.")

    # Add related_name to resolve the conflict with default AbstractUser fields
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    date_of_birth = models.DateField(
        null=True, blank=True, help_text="Optional date of birth for the user.")
    profile_picture = models.ImageField(
        upload_to="profiles/", null=True, blank=True, help_text="Optional profile picture.")

    def __str__(self):
        return self.username


class Category(models.Model):
    """
    Model for product categories with slug support.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            generated_slug = slugify(self.name)
            while Category.objects.filter(slug=generated_slug).exists():
                generated_slug = f"{generated_slug}-{Category.objects.filter(slug__startswith=generated_slug).count() + 1}"
            self.slug = generated_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for products with stock tracking and image support.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            generated_slug = slugify(self.name)
            while Product.objects.filter(slug=generated_slug).exists():
                generated_slug = f"{generated_slug}-{Product.objects.filter(slug__startswith=generated_slug).count() + 1}"
            self.slug = generated_slug
        self.availability = self.stock > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    """
    Model for order statuses to allow flexibility and easy updates.
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model for customer orders with status and total price tracking.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        OrderStatus, related_name="orders", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    """
    Model for items in an order, linked to products and quantities.
    """
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
