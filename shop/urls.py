from django.urls import path
from .views.views import *
from .views.product_views import *
from .views.auth_views import *
from .views.wishlist_views import *
from .views.cart_views import *
from .views.order_views import *
from .views.payment import *
from .views.order_history_views import view_order_history

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
    path('delete/item/from/cart/<int:cart_item_id>',delete_item_from_cart,name="delete_item_from_cart"),

    path('order_details/address',AddressView.as_view(),name="order_details_address"),
    
    path('order_details/process/<int:addr>',OrderProcessView.as_view(),name="order_details_process"),

    path('order/history',view_order_history,name="order_history"),

    path('payment/', payment),
    path('response/', response),
]
