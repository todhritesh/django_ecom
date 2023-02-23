from django.db import models
from datetime import datetime

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
    

