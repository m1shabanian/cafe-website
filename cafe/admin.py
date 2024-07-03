from django.contrib import admin
from .models import User, Admin, Product, Order, OrdersProduct, UsersOrders, Storage, Category

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrdersProduct)
admin.site.register(UsersOrders)
admin.site.register(Storage)