from django.contrib import admin
from .models import Product, Category, Order, OrderProduct, Review, ProductCategory

admin.site.site_header = 'E-Commerce Admin'
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Review)
admin.site.register(ProductCategory)
