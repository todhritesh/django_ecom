from django.db import models
from .models import BaseModel
from .product_models import Product
from django.contrib.auth.models import User

class WishList(BaseModel):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.product.product_title
    
    
