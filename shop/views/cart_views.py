from ..models.cart_models import *
from ..models.product_models import Product
from django.shortcuts import render , redirect 
from django.http import JsonResponse
import json
from django.db.models import F, ExpressionWrapper, FloatField , Value , Sum
from django.db.models.functions import Concat
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from ..helper import has_items_in_cart
from django.urls import reverse_lazy


def is_cart_item_exist(cart):
    if(not CartItem.objects.filter(cart=cart).count()):
        context = {}
        context['total_qty'] = 0
        context['cart_items'] = []
        context['cart_amount'] = round(0,2)
        return (True,context)
    return (False,{})

def add_item_to_cart(req,product_id):
    user = req.user
    cart , is_cart_created = Cart.objects.get_or_create(user=user)
    product = Product.objects.get(pk=product_id)
    cart_item , is_cart_item_created = CartItem.objects.get_or_create(cart=cart,product=product)
    context = {}
    if not is_cart_item_created:
        cart_item.qty = cart_item.qty +1
        cart_item.save()
    if(req.GET.get('from_cart_page',None)!=None):
        cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=ExpressionWrapper(F('product__price') * F('qty'), output_field=FloatField()) ,
            product_title=F('product__product_title'),
            product_price=F('product__price'),
            product_image=F('product__image')
        )
        cart_amount = cart_items.aggregate(Sum('total_price'))['total_price__sum']
        context['cart_amount'] = round(cart_amount,2)
        qs = cart_items
        cart_items = list(qs.values())
        context['cart_items'] = cart_items
    total_qty = cart.total_quantity()
    context['total_qty'] = total_qty
    return JsonResponse(context)

def remove_item_from_cart(req,product_id):
    user = req.user
    cart , is_cart_created = Cart.objects.get_or_create(user=user)
    product = Product.objects.get(pk=product_id)
    cart_item , is_cart_item_created = CartItem.objects.get_or_create(cart=cart,product=product)
    context = {}
    if cart_item.qty>1:
        cart_item.qty = cart_item.qty -1
        cart_item.save()
    else:
        cart_item.delete()
    
    exist , context = is_cart_item_exist(cart)
    if(exist):
        return JsonResponse(context)


    if(req.GET.get('from_cart_page',None)!=None):
        cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=ExpressionWrapper(F('product__price') * F('qty'), output_field=FloatField()) ,
            product_title=F('product__product_title'),
            # product_id=F('product__id'),
            product_price=F('product__price'),
            product_image=F('product__image')
        )
        cart_amount = cart_items.aggregate(Sum('total_price'))['total_price__sum']
        context['cart_amount'] = round(cart_amount,2)
        qs = cart_items
        cart_items = list(qs.values())
        context['cart_items'] = cart_items
    total_qty = cart.total_quantity()
    context['total_qty'] = total_qty
    return JsonResponse(context)    

def delete_item_from_cart(req , cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart = cart_item.cart
    cart_item.delete()
    context = {}
      
    exist , context = is_cart_item_exist(cart)
    if(exist):
        return JsonResponse(context)

    cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=ExpressionWrapper(F('product__price') * F('qty'), output_field=FloatField()) ,
            product_title=F('product__product_title'),
            product_price=F('product__price'),
            product_image=F('product__image')
        )

    cart_amount = cart_items.aggregate(Sum('total_price'))['total_price__sum']
    context['cart_amount'] = round(cart_amount,2)
    qs = cart_items
    cart_items = list(qs.values())
    context['cart_items'] = cart_items
    total_qty = cart.total_quantity()
    context['total_qty'] = total_qty
    return JsonResponse(context)

@user_passes_test(has_items_in_cart,login_url=reverse_lazy('view_cart'))
def view_cart(req):
    context = {}
    user = req.user
    cart , _ = Cart.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=ExpressionWrapper(F('product__price') * F('qty'), output_field=FloatField()))
    cart_amount = cart_items.aggregate(Sum('total_price'))['total_price__sum']
    context['cart_amount'] = round(cart_amount or 0,2)
    context['cart_items'] = cart_items
    return render(req, 'pages/cart.html',context=context)