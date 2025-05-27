from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Product, Category, Order, OrderItem, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter, ProductFilter, CategoryFilter, OrderFilter, OrderItemFilter, ReviewFilter
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
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Operações relacionadas as categorias"
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    permission_classes = [IsAdminUser]
    
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
    summary="Operações relacionadas aos OrderItem"
)
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderItemFilter
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
