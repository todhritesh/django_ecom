from django.shortcuts import render , redirect
from ..models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required , user_passes_test
from django.urls import reverse_lazy
from django.db.models import Case , When , BooleanField , Q


def products(req):
    context = {}
    user = req.user
    categories = Category.objects.all()
    products = ''
    cat = req.GET.get('category',None)
    if(cat!=None):
        context['cat'] = cat
        products = Product.objects.filter(category__slug=cat)
    elif req.GET.get('search',None) != None:
        search = req.GET.get('search',None)
        context['search'] = search
        products = Product.objects.filter(Q(product_title__icontains=search)|Q(category__title__icontains=search))
    else:
        products = Product.objects.all()

    if user.is_authenticated:
        products = products.annotate(isWishlisted=Case(
                    When(wishlist__user=user , then = True) ,
                    default=False,
                    output_field=BooleanField()
                ))

    paginator = Paginator(products, 50)
    pg_no = req.GET.get('page',1)
    data = paginator.get_page(pg_no)
    context['data'] = data
    context['categories'] = categories

    return render(req, 'pages/products.html',context=context)

def single_product(req,slug,id):
    context = {}
    
    categories = Category.objects.all()
    context['categories'] = categories
    context['product'] = Product.objects.get(pk=id)
    context['related_products'] = Product.objects.exclude(pk=id)[:50]

    return render(req, 'pages/single_product.html',context=context)
