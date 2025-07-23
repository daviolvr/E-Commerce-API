from django.db import models
from django.db.models import (
    CharField,
    PositiveSmallIntegerField,
    DateTimeField,
    BooleanField,
    TextField,
    DecimalField,
    PositiveIntegerField,
    ForeignKey,
    OneToOneField,
    ManyToManyField,
    FloatField,
    Sum,
    F,
)
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = CharField(max_length=45, unique=True)
    description = TextField(null=False)
    price = DecimalField(max_digits=10, decimal_places=2)
    categories = ManyToManyField("Category", related_name="products")
    stock = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        return (
            self.stock > 0
        )  # Pra garantir que haja um calculo real e evitar erro em caso de alteração manual no banco

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=30, unique=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("S", "Shipped"),
        ("D", "Delivered"),
        ("C", "Canceled"),
    ]

    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = CharField(max_length=1, choices=STATUS_CHOICES, default="P")
    total = DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"


class OrderProduct(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        db_table = "order_product"
        verbose_name = "Order_Product"

    def __str__(self):
        return f"OrderProduct #{self.id}"


class Review(models.Model):
    RATING_CHOICES = [
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★"),
    ]

    product = ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = PositiveSmallIntegerField(
        choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "product"]
        db_table = "reviews"

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Cart(models.Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"{self.user.username} Cart"


class CartProduct(models.Model):
    cart = ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.quantity > self.product.stock:
            raise ValueError(
                f"Cannot add {self.quantity} units of {self.product.name}. Only {self.product.stock} left in stock."
            )
        super().save(*args, **kwargs)

    class Meta:
        db_table = "cart_product"
        verbose_name = "Cart_Product"

    def __str__(self):
        return f"CartProduct #{self.id}"


class Address(models.Model):
    user = ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses"
    )
    recipient_name = CharField(max_length=100)  # Nome do destinatário
    street = CharField(max_length=255)
    number = CharField(max_length=10)
    complement = CharField(max_length=100, blank=True, null=True)
    city = CharField(max_length=100)
    state = CharField(max_length=100)
    country = CharField(max_length=100, default="Brazil")
    is_default = BooleanField(default=False)  # Para indicar se é o endereço principal
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "addresses"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.recipient_name}, {self.street}, {self.number}, {self.city} - {self.state}"

    def save(self, *args, **kwargs):
        if self.is_default:
            # Garantir que exista apenas um endereço padrão por usuário
            Address.objects.filter(user=self.user, is_default=True).exclude(
                pk=self.pk
            ).update(is_default=False)
        super().save(*args, **kwargs)


class Shipping(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
    ]

    order = OneToOneField(Order, on_delete=models.CASCADE)
    address = ForeignKey(Address, on_delete=models.PROTECT)
    tracking_number = CharField(max_length=100, unique=True, blank=True, null=True)
    status = CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    shipped_at = DateTimeField(blank=True, null=True)
    delivered_at = DateTimeField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "shipping"
        verbose_name = "Shipping"
        verbose_name_plural = "Shippings"

    def __str__(self):
        return f"Shipping for Order {self.order.id} - {self.tracking_number or 'No Tracking'}"


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("Pix", "Pix"),
        ("Credit Card", "Credit Card"),
    ]
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed"),
        ("Refunded", "Refunded"),
    ]

    order = OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = CharField(max_length=100, unique=True, blank=True, null=True)
    payment_method = CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = CharField(max_length=20, choices=STATUS_CHOICES)
    paid_at = DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.payment_method
