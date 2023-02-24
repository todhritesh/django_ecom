from django.shortcuts import render
from .models import *

def home(req):
    context = {}
    context['categories'] = Category.objects.all()
    return render(req, 'pages/home.html',context=context)