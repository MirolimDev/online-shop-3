from django.urls import path

from .views import *

urlpatterns = [ 
    path('add_to_cart/', add_to_cart, name='add-to-cart'),
]