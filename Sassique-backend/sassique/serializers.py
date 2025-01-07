from rest_framework import serializers
from .models import Category, Product, Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Nested items
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    user = UserSerializer(read_only=True)  # Include user details

    class Meta:
        model = Order
        fields = ["id", "user", "status", "created_at", "total_price", "items"]

    def validate(self, attrs):
        """
        Validate if the user is authenticated before creating an order.
        """
        request = self.context.get('request')
        if not request or not request.user or not request.user.is_authenticated:
            raise serializers.ValidationError(
                "You must be logged in to place an order.")
        return attrs

    def create(self, validated_data):
        """
        Override create to handle order creation with nested items.
        """
        request = self.context['request']
        items_data = request.data.get("items", [])
        order = Order.objects.create(user=request.user, **validated_data)

        total_price = 0
        for item_data in items_data:
            try:
                product = Product.objects.get(id=item_data["product_id"])
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    f"Product with ID {item_data['product_id']} does not exist.")

            quantity = item_data["quantity"]

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Product '{product.name}' does not have enough stock. Available: {product.stock}"
                )

            # Deduct stock and add item to order
            product.stock -= quantity
            product.save()
            OrderItem.objects.create(
                order=order, product=product, quantity=quantity)

            total_price += product.price * quantity

        order.total_price = total_price
        order.save()
        return order
