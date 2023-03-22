from django.db import models
from django.contrib.auth.models import User
from .models import BaseModel
from .product_models import Product

class Address(BaseModel):
    name = models.CharField( max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200 , blank=True , null=True)
    flat_no = models.CharField(max_length=10)
    mobile_1 = models.CharField(max_length=13)
    mobile_2 = models.CharField(max_length=13 , blank=True , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

STATUS = (('PENDING','PENDING'),('SUCCESS','SUCCESS'),('FAILED','FAILED'))

class Order(BaseModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField( max_length=50 , choices=STATUS,default=STATUS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField()

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return self.product.product_title + ' - '+ str(self.qty)
    

class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    mode_of_payment = models.CharField(max_length=20,choices=(('cash_on_delivery','cash_on_delivery'),('upi','upi')))
    status = models.CharField( max_length=50 , choices=STATUS,default=STATUS[0][0])
