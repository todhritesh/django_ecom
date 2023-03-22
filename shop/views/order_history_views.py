from ..models.cart_models import *
from ..models.product_models import Product
from django.shortcuts import render , redirect 
from django.http import JsonResponse
import json
from django.db.models import F, ExpressionWrapper, FloatField , Value , Sum
from django.db.models.functions import Concat
from django.conf import settings
from ..models.order_models import *

def view_order_history(req):
    context = {}
    user = req.user
    orders = Order.objects.filter(user=req.user).prefetch_related('items')
    context['orders'] = orders
    print(str(orders))
    return render(req, 'pages/order_history.html',context=context)
    