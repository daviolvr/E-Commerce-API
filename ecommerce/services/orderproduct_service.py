from ecommerce.models import OrderProduct, Product, Order
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.models import F, Sum, DecimalField
from django.db import transaction

class OrderProductService:

    @staticmethod
    def create_order_product(data):
        product = get_object_or_404(Product, pk=data['product'])
        order = get_object_or_404(Order, pk=data['order'])
        quantity = data['quantity']

        if quantity <= 0:
            raise ValidationError("'quantity' must be greater than 0.")

        if product.stock < quantity:
            raise ValidationError(f"Not enough stock. Available: {product.stock}")

        # Atualiza estoque
        product.stock -= quantity
        product.save()

        price = product.price * quantity

        # Cria o pedido
        order_product = OrderProduct.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

        return order_product
    

    @staticmethod
    @transaction.atomic
    def remove_order_product(order_product_id: int) -> None:
        try:
            order_product = OrderProduct.objects.get(pk=order_product_id)
        except OrderProduct.DoesNotExist:
            raise ValueError("OrderProduct not found")
        
        product = order_product.product
        order = order_product.order

        # Restore stock
        product.stock += order_product.quantity
        product.save(update_fields=['stock'])

        # Remove OrderProduct
        order_product.delete()

        # Update order total
        OrderProductService.update_order_total(order)


    @staticmethod
    def update_order_total(order: Order) -> None:
        total = order.items.aggregate(
            total=Sum(F('price') * F('quantity'), output_field=DecimalField()) 
        )['total'] or 0
        order.total = total
        order.save(update_fields=['total'])

