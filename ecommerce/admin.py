from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Review

admin.site.site_header = 'E-Commerce Admin'
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
