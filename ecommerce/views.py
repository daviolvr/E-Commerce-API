from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Product, Category, Order, OrderItem, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    summary="Operações relacionadas aos usuários",
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


@extend_schema(
    summary="Operações relacionadas aos produtos",
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


@extend_schema(
    summary="Operações relacionadas as categorias",
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    

class OrderViewSet(viewsets.ViewSet):
    @extend_schema(
            summary="Cria um pedido",
            description="Cria e retorna o produto gerado"
    )
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @extend_schema(
            summary="Lista todos os pedidos",
            description="Retorna uma lista completa de todos os pedidos ativos no sistema"
    )
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Retorna o pedido especificado",
            description="Retorna o pedido especificado como parâmetro"
    )
    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Deleta o pedido especificado",
            description="Deleta o pedido passado como parâmetro"
    )
    def destroy(self, request, pk=None):
        queryset = Order.objects.all()
        order= get_object_or_404(queryset, pk=pk)
        order.delete()
        return Response(status=204)
    

class OrderItemViewSet(viewsets.ViewSet):
    @extend_schema(
            summary="Cria um OrderItem",
            description="Cria e retorna o OrderItem gerado"
    )
    def create(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @extend_schema(
            summary="Lista todos os OrderItem",
            description="Retorna todos os OrderItem ativos no sistema"
    )
    def list(self, request):
        queryset = OrderItem.objects.all()
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Retorna o OrderItem especificado",
            description="Retorna o OrderItem especificado como parâmetro"
    )
    def retrieve(self, request, pk=None):
        queryset = OrderItem.objects.all()
        order_item = get_object_or_404(queryset, pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Deleta o OrderItem especificado",
            description="Deleta o OrderItem passado como parâmetro"
    )
    def destroy(self, request, pk=None):
        queryset = OrderItem.objects.all()
        order_item = get_object_or_404(queryset, pk=pk)
        order_item.delete()
        return Response(status=204)


class ReviewViewSet(viewsets.ViewSet):
    @extend_schema(
            summary="Cria uma Avaliação",
            description="Cria e retorna a avaliação gerada"
    )
    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @extend_schema(
            summary="Lista todas as avaliações",
            description="Retorna todas as avaliações ativas no sistema"
    )
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Retorna a avaliação especificada",
            description="Retorna a avaliação especificada como parâmetro"
    )
    def retrieve(self, request, pk=None):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        serializer = OrderItemSerializer(review)
        return Response(serializer.data)
    
    @extend_schema(
            summary="Deleta a avaliação especificada",
            description="Deleta a avaliação passada como parâmetro"
    )
    def destroy(self, request, pk=None):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        review.delete()
        return Response(status=204)
