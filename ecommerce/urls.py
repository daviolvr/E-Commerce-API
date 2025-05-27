from django.urls import path

urlpatterns = [
    # User
    path("users/register/", ), # POST
    path("users/<int:pk>/", ), # GET, PUT
    path("users/all/", ), # GET tambem, para listar todos os usuarios
    path("users/<int:pk>/delete/", ), # DELETE

    # Products
    path("products/register/", ), # POST
    path("products/<int:pk>/", ), # GET, PUT
    path("products/all/", ), # GET tambem, para listar todos os produtos
    path("products/<int:pk>/delete/", ), # DELETE

    # Category
    path("categories/register/", ), # POST
    path("categories/<int:pk>/", ), # GET, PUT
    path("categories/all", ), # GET tambem, para listar todas as categorias
    path("categories/<int:pk>/delete/", ), # DELETE

    # Order
    path("orders/create/", ), # POST
    path("orders/<int:pk>/", ), # GET, por enquanto pedidos nao poderao ser alterados
    path("orders/all", ), # GET tambem, para listar todos os pedidos
    path("orders/<int:pk>/delete/", ), # DELETE

    # OrderItem
    path("order-item/create/", ), # POST
    path("order-item/<int:pk>/", ), # GET
    path("order-item/<int:product_id>/", ), # GET tambem, mas pra obter o conjunto de pedidos que possuem determinado produto
    path("order-item/all/", ), # GET tambem, para listar todos os pedidos e itens relacionados
    path("order-item/<int:pk>/", ), # DELETE

    # Review
    path("reviews/create/", ), # POST
    path("reviews/<int:pk>/", ), # GET
    path("reviews/<int:user_id/", ), # GET tambem, mas pra obter o conjunto de reviews de um determinado usuario
    path("reviews/<int:product_id>/", ), # GET tambem, mas pra obter o conjunto de reviews de um determinado produto
    path("reviews/<int:pk>/delete/", ), # DELETE
]