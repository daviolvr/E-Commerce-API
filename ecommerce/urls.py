from django.urls import path

urlpatterns = [
    # Products
    path("product/register/", ), # POST
    path("product/<int:pk>/", ), # GET, PUT
    path("product/<int:pk>/delete/", ), # DELETE

    # Category
    path("category/register/", ), # POST
    path("category/<int:pk>/", ), # GET, PUT
    path("category/<int:pk>/delete/", ), # DELETE

    # Order
    path("order/create/", ), # POST
    path("order/<int:pk>/", ), # GET, por enquanto pedidos nao poderao ser alterados
    path("order/<int:pk>/delete/", ), # DELETE

    # OrderItem
    path("order-item/create/", ), # POST
    path("order-item/<int:pk>/", ), # GET
    path("order-item/<int:product_id>/", ), # GET tambem, mas pra obter o conjunto de pedidos que possuem determinado produto
    path("order-item/<int:pk>/", ), # DELETE

    # Review
    path("review/create/", ), # POST
    path("review/<int:pk>/", ), # GET
    path("review/<int:user_id/", ), # GET tambem, mas pra obter o conjunto de reviews de um determinado usuario
    path("review/<int:product_id>/", ), # GET tambem, mas pra obter o conjunto de reviews de um determinado produto
    path("review/<int:pk>/delete/", ), # DELETE
]