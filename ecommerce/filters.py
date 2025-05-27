from django_filters import FilterSet, CharFilter, BooleanFilter, NumberFilter
from django.contrib.auth.models import User
from .models import Product, Category, Order, OrderItem, Review


class UserFilter(FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProductFilter(FilterSet):
    category = NumberFilter(field_name='category')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    in_stock = BooleanFilter(field_name='in_stock')

    class Meta:
        model = Product
        fields = ['category', 'name', 'in_stock']


class CategoryFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class OrderFilter(FilterSet):
    user = NumberFilter(field_name='user')
    status = CharFilter(field_name='status', lookup_expr='iexact')
    payment_status = CharFilter(field_name='payment_status', lookup_expr='iexact')

    class Meta:
        model = Order
        fields = ['user', 'status', 'payment_status']


class OrderItemFilter(FilterSet):
    order = NumberFilter(field_name='order')
    product = NumberFilter(field_name='product')

    class Meta:
        model = OrderItem
        fields = ['order', 'product']


class ReviewFilter(FilterSet):
    product = NumberFilter(field_name='product')
    user = NumberFilter(field_name='user')
    rating = NumberFilter(field_name='rating', lookup_expr='iexact')
    min_rating = NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'min_rating', 'max_rating']
