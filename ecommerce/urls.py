from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (UserViewSet, ProductViewSet, CategoryViewSet, OrderViewSet, 
                    OrderProductViewSet, ReviewViewSet, CartViewSet, CartProductViewSet,
                    ShippingViewSet, PaymentViewSet, AddressViewSet)

urlpatterns = [
    # User
    path("users/register/", UserViewSet.as_view({'post': 'create'})), # POST
    path("users/<int:pk>/", UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})), # GET, PUT, PATCH
    path("users/", UserViewSet.as_view({'get': 'list'})), # GET tambem, para listar todos os usuarios
    path("users/<int:pk>/delete/", UserViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Products
    path("products/register/", ProductViewSet.as_view({'post': 'create'})), # POST
    path("products/<int:pk>/", ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})), # GET, PUT, PATCH
    path("products/", ProductViewSet.as_view({'get': 'list'})), # GET tambem, para listar todos os produtos
    path("products/<int:pk>/delete/", ProductViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Category
    path("categories/register/", CategoryViewSet.as_view({'post': 'create'})), # POST
    path("categories/<int:pk>/", CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})), # GET, PUT, PATCH
    path("categories/", CategoryViewSet.as_view({'get': 'list'})), # GET tambem, para listar todas as categorias
    path("categories/<int:pk>/delete/", CategoryViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Order
    path("orders/create/", OrderViewSet.as_view({'post': 'create'})), # POST
    path("orders/<int:pk>/", OrderViewSet.as_view({'get': 'retrieve'})), # GET, por enquanto pedidos nao poderao ser alterados
    path("orders/", OrderViewSet.as_view({'get': 'list'})), # GET tambem, para listar todos os pedidos
    path("orders/<int:pk>/delete/", OrderViewSet.as_view({'delete': 'destroy'})), # DELETE

    # OrderProduct
    path("order-product/create/", OrderProductViewSet.as_view({'post': 'create'})), # POST
    path("order-product/<int:pk>/", OrderProductViewSet.as_view({'get': 'retrieve'})), # GET
    path("order-product/product/<int:product_id>/", OrderProductViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de pedidos que possuem determinado produto
    path("order-product/", OrderProductViewSet.as_view({'get': 'list'})), # GET tambem, para listar todos os pedidos e itens relacionados
    path("order-product/<int:pk>/delete/", OrderProductViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Review
    path("reviews/create/", ReviewViewSet.as_view({'post': 'create'})), # POST
    path("reviews/<int:pk>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET
    path("reviews/user/<int:user_id>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de reviews de um determinado usuario
    path("reviews/product/<int:product_id>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de reviews de um determinado produto
    path("reviews/<int:pk>/delete/", ReviewViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Cart
    path("carts/create/", CartViewSet.as_view({'post': 'create'})), # POST
    path("carts/<int:pk>/", CartViewSet.as_view({'get': 'retrieve'})),
    path("carts/", CartViewSet.as_view({'get': 'list'})),
    path("carts/<int:pk>/delete/", CartViewSet.as_view({'delete': 'destroy'})),

    # CartProduct
    path("cart-product/create/", CartProductViewSet.as_view({'post': 'create'})),
    path("cart-product/<int:pk>/", CartProductViewSet.as_view({'get': 'retrieve'})),
    path("cart-product/", CartProductViewSet.as_view({'get': 'list'})),
    path("cart-product/<int:pk>/delete/", CartProductViewSet.as_view({'delete': 'destroy'})),

    # Shipping
    path("shippings/create/", ShippingViewSet.as_view({'post': 'create'})),
    path("shippings/<int:pk>/", ShippingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
    path("shippings/", ShippingViewSet.as_view({'get': 'list'})),
    path("shippings/<int:pk>/delete/", ShippingViewSet.as_view({'delete': 'destroy'})),

    # Payment
    path("payments/create/", PaymentViewSet.as_view({'post': 'create'})),
    path("payments/<int:pk>/", PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
    path("payments/", PaymentViewSet.as_view({'get': 'list'})),
    path("payments/<int:pk>/delete/", PaymentViewSet.as_view({'delete': 'destroy'})),

    # Address
    path("addresses/create/", AddressViewSet.as_view({'post': 'create'})),
    path("addresses/<int:pk>/", AddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
    path("addresses/", AddressViewSet.as_view({'get': 'list'})),
    path("addresses/<int:pk>/delete/", AddressViewSet.as_view({'delete': 'destroy'})),

    # Swagger
    path("schema/", SpectacularAPIView.as_view(), name='schema'), # Gera o schema OpenAPI em YAML/JSON
    path("docs/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Swagger UI
    path("redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Redoc

    # JWT
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]