from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    search_fields = ('name', 'price')
    list_display = ('name', 'price', 'category')
    list_filter = ('name', 'category')



class AdminCategory(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', )
    list_filter = ('name',)


class AdminCustomer(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name', 'last_name', 'email')


class AdminOrder(admin.ModelAdmin):
    search_fields = ('cutomer', 'product')
    list_display = ('customer', 'product')
    list_filter = ('customer', 'product')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
