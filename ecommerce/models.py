from django.db import models
from django.db.models import (CharField, PositiveSmallIntegerField, DateTimeField, BooleanField,
                              TextField, DecimalField, PositiveIntegerField, ForeignKey,
                              OneToOneField, ManyToManyField, FloatField, Sum, F)
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = CharField(max_length=45, unique=True)
    description = TextField(null=False)
    price = DecimalField(max_digits=10, decimal_places=2)
    categories = ManyToManyField('Category', related_name='products')
    stock = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        return self.stock > 0 # Pra garantir que haja um calculo real e evitar erro em caso de alteração manual no banco

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
    
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    total = DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    # Para atualizar automaticamente ao adicionar ou remover produtos 
    def update_total(self):
        total = self.items.aggregate(
            total=Sum(F('price') * F('quantity'), output_field=FloatField())
        )['total'] or 0
        self.total = total
        self.save(update_fields=['total'])

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"


class OrderProduct(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.price
    
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price # Pra garantir que não cause inconsistência se o preço do produto for alterado depois do pedido ser feito
    
        # Caso seja um objeto novo (ainda não salvo no banco)
        if not self.pk:
            if self.product.stock >= self.quantity:
                self.product.stock -= self.quantity
                self.product.save()
            else:
                raise ValueError(f"Insufficient stock for {self.product.name}")
        else:
            # Atualização de quantidade existente
            previous = OrderProduct.objects.get(pk=self.pk)
            difference = self.quantity - previous.quantity

            if difference > 0:
                if self.product.stock >= difference:
                    self.product.stock -= difference
                    self.product.save()
                else:
                    raise ValueError(f"Insufficient stock for {self.product.name}")
            elif difference < 0:
                self.product.stock += abs(difference)
                self.product.save()

        super().save(*args, **kwargs)
        self.order.update_total()

    def delete(self, *args, **kwargs):
        # Quando um OrderProduct é deletado, devolve o estoque
        self.product.stock += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)
        self.order.update_total()
    
    class Meta:
        db_table = 'order_product'


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
    review_text = TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']
        db_table = 'reviews'

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    

class Cart(models.Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table='cart'


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
        db_table='cart_product'


class Shipping(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    order = OneToOneField(Order, on_delete=models.CASCADE)
    address = TextField()
    tracking_number = CharField(max_length=100, blank=True, null=True)
    status = CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    shipped_at = DateTimeField(blank=True, null=True)
    delivered_at = DateTimeField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shipping'


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('Pix', 'Pix'),
        ('Credit Card', 'Credit Card'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]

    order = OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = CharField(max_length=20, choices=STATUS_CHOICES)
    paid_at = DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'payment'
