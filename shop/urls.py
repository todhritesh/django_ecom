from django.urls import path
from .views.views import *
from .views.product_views import *
from .views.auth_views import *
from .views.wishlist_views import *
from .views.cart_views import *

urlpatterns = [
    path('',home,name="home"),
    path('products',products,name="products"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('logout',logout,name="logout"),
    path('product/<slug>/<int:id>',single_product,name="single_product"),

    path('handle_wishlist/<id>',handle_wishlist,name='handle_wishlist'),
    path('wishlists',show_wishlists,name='show_wishlists'),

    path('add/to/cart/<int:product_id>/',add_item_to_cart,name="add_item_to_cart"),
    path('remove/from/cart/<int:product_id>/',remove_item_from_cart,name="remove_item_from_cart"),
    path('view/cart',view_cart,name="view_cart"),
]
