from ..models.cart_models import *
from ..models.models import Product
from django.shortcuts import render , redirect 
from django.http import JsonResponse

def add_item_to_cart(req,product_id):
    user = req.user
    cart , is_cart_created = Cart.objects.get_or_create(user=user)
    product = Product.objects.get(pk=product_id)
    cart_item , is_cart_item_created = CartItem.objects.get_or_create(cart=cart,product=product)
    if not is_cart_item_created:
        cart_item.qty = cart_item.qty +1
        cart_item.save()
    
    total_qty = cart.total_quantity()
    return JsonResponse({'total_qty':total_qty})

def remove_item_from_cart(req):
    pass    

def delete_item_from_cart(req):
    pass