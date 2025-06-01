from django.contrib import admin
from .models import Product, Category, Order, OrderProduct, Review, Cart, CartProduct, Shipping, Payment

admin.site.site_header = 'E-Commerce Admin'
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Shipping)
admin.site.register(Payment)
