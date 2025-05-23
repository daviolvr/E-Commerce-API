from django.db import models
from django.db.models import (CharField, PositiveSmallIntegerField, DateTimeField, 
                              TextField, DecimalField, PositiveIntegerField, ForeignKey)
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = CharField(max_length=45, unique=True)
    description = TextField(null=False)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = PositiveIntegerField(default=0)
    category = ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=30, unique=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Canceled'),
    ]
    PAYMENT_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
        ('R', 'Refunded'),
    ]
    
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    payment_status = CharField(max_length=1, choices=PAYMENT_CHOICES, default='P')
    total = DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"


class OrderItem(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.price
    
    class Meta:
        db_table = 'order_item'


class Review(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    product = ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)] 
    )
    review_text = TextField()
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']
        db_table = 'reviews'

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

