from django.db import models
from django.contrib.auth.models import User
    
class Item(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    category_id = models.CharField(max_length=200) # change this to foreign key for category
    tags = models.TextField(max_length=50)
    sku = models.CharField(max_length=200)
    status =  models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at','-modified_at','id')
    
class Category(models.Model):
    # id = models.IntegerField(primary=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at','-modified_at','id')

class UserItem(models.Model):
    # id = models.CharField(max_length=200,primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    modified_at =  models.DateTimeField(auto_now=True)
    
    # class Meta:
    #     ordering = ('-created_at','-modified_at','id')
    