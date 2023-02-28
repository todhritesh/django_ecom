from django.contrib.auth.decorators import login_required
from ..models import WishList , Product
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from ..helper import *
from django.contrib.auth import login as handle_login , logout as handle_logout , authenticate
from django.http import JsonResponse
from django.db.models import Value , BooleanField

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
        return JsonResponse({'success':False,'location':'login'},status=500)
    return JsonResponse(data)


def show_wishlists(req):
    context = {}
    user = req.user
    wishlists = WishList.objects.filter(user=user).select_related('product')
    print(wishlists)
    context['wishlists'] = wishlists
    return render(req, 'pages/wishlist.html',context=context)
