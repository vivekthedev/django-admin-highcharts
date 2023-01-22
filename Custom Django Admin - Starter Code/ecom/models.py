from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import uuid

class User(AbstractUser):
    country = CountryField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    is_digital = models.BooleanField(default=False)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_on = models.DateField(auto_now_add=True)
