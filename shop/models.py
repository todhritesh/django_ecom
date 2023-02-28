from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    # class Meta:
        # db_table = 'categories'
    
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50,blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(BaseModel):
    product_title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    image = models.ImageField(upload_to='products/',blank=True)

    def __str__(self):
        return self.product_title


class Account(BaseModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE,related_name='account')
    phone = models.CharField( max_length=15,blank=True)

    def __str__(self):
        return self.user.username


class WishList(BaseModel):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.product.product_title
    
    

