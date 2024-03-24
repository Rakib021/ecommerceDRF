from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CartItemViewSet, OrderViewSet, DailyDataViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dailydata', DailyDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
