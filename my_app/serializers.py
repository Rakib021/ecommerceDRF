from rest_framework import serializers
from .models import User, Product, Cart, CartItem, Order, DailyData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','password', 'is_buyer', 'is_seller']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DailyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyData
        fields = '__all__'
