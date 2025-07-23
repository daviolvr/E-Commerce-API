from django_filters import FilterSet, CharFilter, BooleanFilter, NumberFilter
from django.contrib.auth.models import User
from .models import (
    Product,
    Category,
    Order,
    OrderProduct,
    Review,
    Cart,
    CartProduct,
    Shipping,
    Payment,
    Address,
)


class UserFilter(FilterSet):
    username = CharFilter(field_name="username", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="iexact")

    class Meta:
        model = User
        fields = ["username", "email"]


class ProductFilter(FilterSet):
    category = NumberFilter(field_name="category")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    in_stock = BooleanFilter(field_name="in_stock")

    class Meta:
        model = Product
        fields = ["category", "name", "in_stock"]


class CategoryFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ["name"]


class OrderFilter(FilterSet):
    user = NumberFilter(field_name="user")
    status = CharFilter(field_name="status", lookup_expr="iexact")
    payment_status = CharFilter(field_name="payment_status", lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ["user", "status", "payment_status"]


class OrderProductFilter(FilterSet):
    order = NumberFilter(field_name="order")
    product = NumberFilter(field_name="product")

    class Meta:
        model = OrderProduct
        fields = ["order", "product"]


class ReviewFilter(FilterSet):
    product = NumberFilter(field_name="product")
    user = NumberFilter(field_name="user")
    rating = NumberFilter(field_name="rating", lookup_expr="iexact")
    min_rating = NumberFilter(field_name="rating", lookup_expr="gte")
    max_rating = NumberFilter(field_name="rating", lookup_expr="lte")

    class Meta:
        model = Review
        fields = ["product", "user", "rating", "min_rating", "max_rating"]


class CartFilter(FilterSet):
    user = NumberFilter(field_name="user")

    class Meta:
        model = Cart
        fields = ["user"]


class CartProductFilter(FilterSet):
    cart = NumberFilter(field_name="cart")
    product = NumberFilter(field_name="product")

    class Meta:
        model = CartProduct
        fields = ["cart", "product"]


class ShippingFilter(FilterSet):
    order = NumberFilter(field_name="order")
    address = CharFilter(field_name="address", lookup_expr="icontains")
    tracking_number = CharFilter(field_name="tracking_number", lookup_expr="iexact")
    status = CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = Shipping
        fields = ["order", "address", "tracking_number", "status"]


class PaymentFilter(FilterSet):
    order = NumberFilter(field_name="order")
    payment_method = CharFilter(field_name="payment_method", lookup_expr="iexact")
    status = CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = Payment
        fields = ["order", "payment_method", "status"]


class AddressFilter(FilterSet):
    user = NumberFilter(field_name="user")
    city = CharFilter(field_name="city", lookup_expr="icontains")
    state = CharFilter(field_name="state", lookup_expr="iexact")
    country = CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Address
        fields = ["user", "city", "state", "country"]
