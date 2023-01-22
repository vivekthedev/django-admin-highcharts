from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Order


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "get_full_name", "email", "country")
    list_editable = ("country",)
    list_filter = []
   

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_digital")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "ordered_on")
    
