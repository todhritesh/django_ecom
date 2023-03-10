from .models import BaseModel 
from .product_models import Product
from django.db import models
from django.contrib.auth.models import User

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    def calculate_total_amount(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.product.price * item.qty
        return total

    def total_quantity(self):
        return self.cartitem_set.aggregate(total_quantity=models.Sum('qty'))['total_quantity'] or 0    

class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.product_title + ' - ' + self.qty
    

