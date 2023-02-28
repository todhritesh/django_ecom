from django.urls import path
from .views.views import *
from .views.product_views import *
from .views.auth_views import *
from .views.wishlist_views import *

urlpatterns = [
    path('',home,name="home"),
    path('products',products,name="products"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('logout',logout,name="logout"),
    path('product/<slug>/<int:id>',single_product,name="single_product"),

    path('handle_wishlist/<id>',handle_wishlist,name='handle_wishlist'),
]
