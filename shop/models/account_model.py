from .models import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Account(BaseModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE,related_name='account')
    phone = models.CharField( max_length=15,blank=True)

    def __str__(self):
        return self.user.username
