from django.contrib import admin
from django.db.models.deletion import CASCADE
from .models import  Cart
# Register your models here.

admin.site.register(Cart)