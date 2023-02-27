from django.shortcuts import render , redirect
from .models import *
from django.core.paginator import Paginator
from .forms import SignupForm , LoginForm
from django.contrib.auth import login as handle_login , authenticate 

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
        products = Product.objects.filter(category__slug=cat)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 50)
    pg_no = req.GET.get('page',1)
    data = paginator.get_page(pg_no)
    context = {'data':data,'categories':categories,'cat':cat}

    return render(req, 'pages/products.html',context=context)

def single_product(req,slug,id):
    context = {}
    
    categories = Category.objects.all()
    context['categories'] = categories
    context['product'] = Product.objects.get(pk=id)
    context['related_products'] = Product.objects.exclude(pk=id)[:50]

    return render(req, 'pages/single_product.html',context=context)


def login(req):
    login_form = LoginForm(req.POST or None)
    context = {'login_form':login_form}
    try:

        if req.method=='POST':
            if login_form.is_valid():
                data = login_form.cleaned_data
                user = authenticate(username=data.get('username'),password=data.get('password'))
                if user is not None :
                    handle_login(req, user)
                    return redirect('products')
            raise Exception('Something Went wrong')
    except:
        return render(req , 'pages/login.html',context=context)
    return render(req , 'pages/login.html',context=context)

def signup(req):
    signup_form = SignupForm(req.POST or None)
    context = {'signup_form':signup_form}
    try:

        if req.method=='POST':
            if signup_form.is_valid():
                data = signup_form.cleaned_data
                user = User.objects.create_user(username=data.get('username'),email=data.get('email'),password=data.get('password'))
                Account.objects.create(user=user)
                context['signup_form'] = SignupForm()
                return render(req , 'pages/signup.html',context=context)
            raise Exception('Something Went wrong')
    except:
        return render(req , 'pages/signup.html',context=context)
    return render(req , 'pages/signup.html',context=context)