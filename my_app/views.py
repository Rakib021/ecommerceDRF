from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import User, Product, Cart, CartItem, Order, DailyData
from .serializers import UserSerializer, ProductSerializer, CartItemSerializer, OrderSerializer, DailyDataSerializer,CartSerializer
import requests
from .forms import registerModelForm

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from .mypagination import MyPageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class =  MyPageNumberPagination


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = Product.objects.get(pk=product_id)


        existing_item = CartItem.objects.filter(cart=cart, product=product).first()

        if existing_item:

            existing_item.quantity += int(quantity)
            existing_item.save()
        else:

            new_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        serializer = CartSerializer(cart)
        return Response(serializer.data)






class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            user = self.request.user
            cart = Cart.objects.get(user=user)
            cart_items = cart.items.all()


            total_amount = sum(item.product.price * item.quantity for item in cart_items)


            order = serializer.save(user=user, total_amount=total_amount)


            for item in cart_items:
                order.items.add(item)


            cart.items.clear()


            self.update_daily_revenue(total_amount)

    def update_daily_revenue(self, revenue):
        today = timezone.now().date()
        daily_data, created = DailyData.objects.get_or_create(date=today)

        if not created:
            daily_data.revenue += revenue
            daily_data.save()


class DailyDataViewSet(viewsets.ModelViewSet):
    queryset = DailyData.objects.all()
    serializer_class = DailyDataSerializer


#fetching products from api
# def products(request):

#     products = requests.get('http://127.0.0.1:8000/api/products/').json()
#     return render(request, 'index.html', {'products': products})



# def register(request):
#     if request.method == 'POST':
#         form = registerModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product')
#     else:
#         form = registerModelForm()
#     return render(request, 'register.html', {'form': form,'username': request.user.username})









