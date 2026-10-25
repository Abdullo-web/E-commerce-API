from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    kolichestvo = models.IntegerField(default=0)