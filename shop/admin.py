from django.contrib import admin
from .models.product_models import *
from .models.wishlist_models import *
from .models.order_models import *
from django.utils.html import format_html
from django.urls import reverse
from .models.account_model import Account
from .models.cart_models import *
from .models.order_models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','slug','created_at','edit_category','delete_category')
    search_fields = ('title','description')
    ordering = ('id',)

    def edit_category(self , obj):
        return format_html('<a href="/admin/shop/category/{}/change/">Edit</a>',obj.id)


    def delete_category(self , obj):
        return format_html('<a href="/admin/shop/category/{}/delete/">Delete</a>',obj.id)

    prepopulated_fields = {'slug':('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_title','category','price','discount_price')

    prepopulated_fields = {'slug':('product_title',)}

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id','product','qty')
        
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Account)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Address) 
admin.site.register(Order) 
admin.site.register(OrderItem) 
admin.site.register(Payment) 

