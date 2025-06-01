from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Product, Category, Order, OrderProduct, Review, Cart, CartProduct, Shipping, Payment
from .serializers import (UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer, 
                          OrderProductSerializer, ReviewSerializer, CartSerializer, CartProductSerializer,
                          ShippingSerializer, PaymentSerializer)
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .filters import (UserFilter, ProductFilter, CategoryFilter, OrderFilter, 
                      OrderProductFilter, ReviewFilter, CartFilter, CartProductFilter,
                      ShippingFilter, PaymentFilter)
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly


@extend_schema(
    summary="Operações relacionadas aos usuários"
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas aos produtos"
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(
    summary="Operações relacionadas as categorias"
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    permission_classes = [IsAdminOrReadOnly]
    
@extend_schema(
    summary="Operações relacionadas aos pedidos"
)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
    permission_classes = [IsAdminUser]
    

@extend_schema(
    summary="Operações relacionadas aos OrderProduct"
)
class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderProductFilter
    permission_classes = [IsAdminUser]
    

@extend_schema(
    summary="Operações relacionadas às avaliações"
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas ao Cart"
)
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartFilter
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas aos CartProduct"
)
class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartProductFilter
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas ao Shipping"
)
class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShippingFilter
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas ao Payment"
)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    permission_classes = [IsAdminUser]
