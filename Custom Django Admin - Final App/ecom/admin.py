from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Order
from django.db.models import Count
from django_countries.fields import Country
from django.shortcuts import render


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "get_full_name", "email", "country")
    list_editable = ("country",)
    list_filter = []
    
    def analytics(self, request):
        users = list(
        User.objects.values_list("country")
        .annotate(country_count=Count("country"))
        .order_by("country")
    )
        countries = [Country(x[0]).name for x in users]
        data = [x[1] for x in users]

        return render(request, "user_analytics.html", {"countries": countries, "data": data, "title":"Users by Country"})

    def get_urls(self):
        urls = super().get_urls()
        from django.urls import path
        custom_urls = [
            path("analytics/", self.analytics),
        ]
        return custom_urls + urls

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_digital")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "ordered_on")
    
