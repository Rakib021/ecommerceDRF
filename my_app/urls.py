from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CartItemViewSet, OrderViewSet, DailyDataViewSet,CartViewSet
from .views import products,register

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dailydata', DailyDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('',products,name='product'),
    path('register/',register,name='register'),
    

]
