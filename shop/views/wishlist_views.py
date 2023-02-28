from django.contrib.auth.decorators import user_passes_test
from ..models import WishList , Product
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from ..helper import *
from django.contrib.auth import login as handle_login , logout as handle_logout , authenticate
from django.http import JsonResponse

def handle_wishlist(req,id):
    try:
        data = {}
        user = req.user
        product = Product.objects.get(pk=id)
        print(product)
        wishlist = WishList.objects.filter(user=user , product=product)
        if(len(wishlist)):
            wishlist[0].delete()
            data = {'success':True,'msg':'removed'}
        else:
            WishList.objects.create(user=user,product=product)
            data = {'success':True,'msg':'added'}
    except:
        return JsonResponse({'success':False})
    return JsonResponse(data)
