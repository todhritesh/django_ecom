from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('products',products,name="products"),
    path('product/<slug>',single_product,name="single_product"),
]
