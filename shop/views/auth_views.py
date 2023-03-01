from django.contrib.auth.decorators import user_passes_test
from ..models.account_model import Account
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from ..forms import SignupForm , LoginForm
from django.urls import reverse_lazy
from ..helper import *
from django.contrib.auth import login as handle_login , logout as handle_logout , authenticate


@user_passes_test(is_logged_in,login_url=reverse_lazy('home'))
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


@user_passes_test(is_logged_in,login_url=reverse_lazy('home'))
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


def logout(req):
    handle_logout(req)
    return redirect('home')
