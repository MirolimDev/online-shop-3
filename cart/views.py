

from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render

from catalog.models import Product
from django.http import JsonResponse

from django.core.exceptions import ObjectDoesNotExist
from .models import Cart

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers



@csrf_exempt
def add_to_cart(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity'))

    product = Product.objects.get(id=product_id)


    try:
        cart = Cart.objects.get(product_id=product_id)
        cart.quantity += quantity
        cart.save()

    except ObjectDoesNotExist:
        cart = Cart.objects.create(product_id=Product.objects.get(id=product_id), quantity=quantity, user_id = User.objects.get(id=1))
        cart.save()

    return JsonResponse({
        "product_id": product.id,
        "product_name": product.name,
        "product_image_url": product.image.url,
        "product_price": product.price,
        "product_old_price": product.old_price
    })




