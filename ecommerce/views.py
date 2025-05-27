from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Product, Category, Order, OrderItem, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    

class OrderViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Order.objects.all()
        order= get_object_or_404(queryset, pk=pk)
        order.delete()
        return Response(status=204)
    

class OrderItemViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def list(self, request):
        queryset = OrderItem.objects.all()
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = OrderItem.objects.all()
        order_item = get_object_or_404(queryset, pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = OrderItem.objects.all()
        order_item = get_object_or_404(queryset, pk=pk)
        order_item.delete()
        return Response(status=204)


class ReviewViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        serializer = OrderItemSerializer(review)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        review.delete()
        return Response(status=204)
