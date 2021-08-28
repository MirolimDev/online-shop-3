from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)