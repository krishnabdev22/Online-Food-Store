from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.feedback import Feedback


class AdminProduct(admin.ModelAdmin):
    list_display = ["name", 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]

class AdminCustomer(admin.ModelAdmin):
    list_display = ["first_name", 'last_name']

class AdminOrder(admin.ModelAdmin):
    list_display = ["date", "customer", "phone", "product", "status"]

class AdminFeedback(admin.ModelAdmin):
    list_display = ["name" , "email"]

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Feedback, AdminFeedback)

