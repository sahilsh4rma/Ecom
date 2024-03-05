from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length =200)
    category = models.CharField(max_length =200)
    price = models.FloatField()
    discounted_price =  models.FloatField()
    decription = models.TextField(max_length =200)
    image = models.CharField(max_length = 500)