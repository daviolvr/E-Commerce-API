from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets, status
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
from .serializers import (
    UserSerializer,
    ProductSerializer,
    CategorySerializer,
    OrderSerializer,
    OrderProductSerializer,
    ReviewSerializer,
    CartSerializer,
    CartProductSerializer,
    ShippingSerializer,
    PaymentSerializer,
    AddressSerializer,
)
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .filters import (
    UserFilter,
    ProductFilter,
    CategoryFilter,
    OrderFilter,
    OrderProductFilter,
    ReviewFilter,
    CartFilter,
    CartProductFilter,
    ShippingFilter,
    PaymentFilter,
    AddressFilter,
)
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
from .services.payment_service import PaymentService
from .services.shipping_service import ShippingService
from .services.orderproduct_service import OrderProductService


@extend_schema_view(
    create=extend_schema(summary="Creates an user", description="Creates a new user."),
    list=extend_schema(
        summary="List all users",
        description="Returns a list of all users in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific user",
        description="Returns an user by ID.",
    ),
    update=extend_schema(
        summary="Update an user",
        description="Updates an user by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update an user",
        description="Partially updates an user's details by its ID.",
    ),
    destroy=extend_schema(
        summary="Delete an user", description="Deletes an user by its ID."
    ),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [IsAdminUser]


@extend_schema_view(
    create=extend_schema(
        summary="Creates a product.",
        description="Creates a new product",
    ),
    list=extend_schema(
        summary="List all products",
        description="Returns a list of all products in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific product",
        description="Returns a product by ID.",
    ),
    update=extend_schema(
        summary="Update a product",
        description="Updates a product by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a product",
        description="Partially updates a product by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a product", description="Deletes a product by its ID."
    ),
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    create=extend_schema(
        summary="Creates a category.",
        description="Creates a new category",
    ),
    list=extend_schema(
        summary="List all category",
        description="Returns a list of all categories in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific category",
        description="Returns a category by ID.",
    ),
    update=extend_schema(
        summary="Update a category",
        description="Updates a category by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a category",
        description="Partially updates a category by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a category", description="Deletes a category by its ID."
    ),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    create=extend_schema(
        summary="Creates an order.",
        description="Creates a new order",
    ),
    list=extend_schema(
        summary="List all order",
        description="Returns a list of all orders in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific order",
        description="Returns a order by ID.",
    ),
    destroy=extend_schema(
        summary="Delete an order", description="Deletes an order by its ID."
    ),
)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
    permission_classes = [IsAdminUser]


@extend_schema_view(
    create=extend_schema(
        summary="Creates an OrderProduct.",
        description="Creates an new OrderProduct",
    ),
    list=extend_schema(
        summary="List all OrderProduct",
        description="Returns a list of all OrderProduct in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an specific OrderProduct",
        description="Returns an OrderProduct by ID.",
    ),
    destroy=extend_schema(
        summary="Delete an OrderProduct",
        description="Deletes an OrderProduct by its ID.",
    ),
)
class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderProductFilter
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        order_product = OrderProductService.create_order_product(request.data)
        serializer = self.get_serializer(order_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        order_product_id = kwargs.get("pk")
        try:
            OrderProductService.remove_order_product(order_product_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    create=extend_schema(
        summary="Creates a category.",
        description="Creates a new category",
    ),
    list=extend_schema(
        summary="List all category",
        description="Returns a list of all categories in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific category",
        description="Returns a category by ID.",
    ),
    destroy=extend_schema(
        summary="Delete a category", description="Deletes a category by its ID."
    ),
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
    permission_classes = [IsAdminUser]


@extend_schema_view(
    create=extend_schema(
        summary="Creates a cart.",
        description="Creates a new cart",
    ),
    list=extend_schema(
        summary="List all carts",
        description="Returns a list of all carts in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific cart",
        description="Returns a cart by ID.",
    ),
    update=extend_schema(
        summary="Update a cart",
        description="Updates a cart by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a cart",
        description="Partially updates a cart by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a cart", description="Deletes a cart by its ID."
    ),
)
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartFilter
    permission_classes = [IsAdminUser]


@extend_schema_view(
    create=extend_schema(
        summary="Creates a CartProduct.",
        description="Creates a new CartProduct",
    ),
    list=extend_schema(
        summary="List all CartProduct",
        description="Returns a list of all CartProduct in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific CartProduct",
        description="Returns a CartProduct by ID.",
    ),
    destroy=extend_schema(
        summary="Delete a CartProduct", description="Deletes a CartProduct by its ID."
    ),
)
class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartProductFilter
    permission_classes = [IsAdminUser]


@extend_schema_view(
    create=extend_schema(
        summary="Creates a shipping.",
        description="Creates a new shipping",
    ),
    list=extend_schema(
        summary="List all shippings",
        description="Returns a list of all shipping in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific shipping",
        description="Returns a shipping by ID.",
    ),
    update=extend_schema(
        summary="Update a shipping",
        description="Updates a shipping by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a shipping",
        description="Partially updates a shipping by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a shipping", description="Deletes a shipping by its ID."
    ),
)
class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShippingFilter
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        tracking_number = ShippingService.generate_tracking_number()
        serializer.save(tracking_number=tracking_number)


@extend_schema_view(
    create=extend_schema(
        summary="Creates a payment.",
        description="Creates a new payment",
    ),
    list=extend_schema(
        summary="List all payments",
        description="Returns a list of all payments in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific payment",
        description="Returns a payment by ID.",
    ),
    update=extend_schema(
        summary="Update a payment",
        description="Updates a payment by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a payment",
        description="Partially updates a payment by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a payment", description="Deletes a payment by its ID."
    ),
)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        transaction_id = PaymentService.generate_transaction_id()
        serializer.save(transaction_id=transaction_id)


@extend_schema_view(
    create=extend_schema(
        summary="Creates a address.",
        description="Creates a new address",
    ),
    list=extend_schema(
        summary="List all addresses",
        description="Returns a list of all addresses in the system.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific address",
        description="Returns a address by ID.",
    ),
    update=extend_schema(
        summary="Update a address",
        description="Updates a address by its ID.",
    ),
    partial_update=extend_schema(
        summary="Partially update a address",
        description="Partially updates a address by its ID",
    ),
    destroy=extend_schema(
        summary="Delete a address", description="Deletes a address by its ID."
    ),
)
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddressFilter
    permission_classes = [IsAdminUser]
