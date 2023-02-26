from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def home(req):
    context = {}
    
    categories = Category.objects.all().prefetch_related('products')
    context['categories'] = categories
    products = {}
    for category in categories:
        products[category.title] = category.products.all()[:10]

    context['products'] = products
    return render(req, 'pages/home.html',context=context)


def products(req):
    categories = Category.objects.all()
    products = ''
    cat = req.GET.get('category',None)
    if(cat!=None):
        products = Product.objects.filter(category=cat)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 50)
    pg_no = req.GET.get('page',1)
    data = paginator.get_page(pg_no)
    context = {'data':data,'categories':categories,'cat':cat}

    return render(req, 'pages/products.html',context=context)