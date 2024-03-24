from rest_framework import viewsets
from .models import User, Product, Cart, CartItem, Order, DailyData
from .serializers import UserSerializer, ProductSerializer, CartItemSerializer, OrderSerializer, DailyDataSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DailyDataViewSet(viewsets.ModelViewSet):
    queryset = DailyData.objects.all()
    serializer_class = DailyDataSerializer
