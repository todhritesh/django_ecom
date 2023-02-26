from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse

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
        
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

