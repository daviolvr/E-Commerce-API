from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import UserViewSet, ProductViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet

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

    # OrderItem
    path("order-item/create/", OrderItemViewSet.as_view({'post': 'create'})), # POST
    path("order-item/<int:pk>/", OrderItemViewSet.as_view({'get': 'retrieve'})), # GET
    path("order-item/<int:product_id>/", OrderItemViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de pedidos que possuem determinado produto
    path("order-item/", OrderItemViewSet.as_view({'get': 'list'})), # GET tambem, para listar todos os pedidos e itens relacionados
    path("order-item/<int:pk>/delete/", OrderItemViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Review
    path("reviews/create/", ReviewViewSet.as_view({'post': 'create'})), # POST
    path("reviews/<int:pk>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET
    path("reviews/<int:user_id>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de reviews de um determinado usuario
    path("reviews/<int:product_id>/", ReviewViewSet.as_view({'get': 'retrieve'})), # GET tambem, mas pra obter o conjunto de reviews de um determinado produto
    path("reviews/<int:pk>/delete/", ReviewViewSet.as_view({'delete': 'destroy'})), # DELETE

    # Swagger
    path("schema/", SpectacularAPIView.as_view(), name='schema'), # Gera o schema OpenAPI em YAML/JSON
    path("docs/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Swagger UI
    path("redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Redoc
]