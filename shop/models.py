from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length =200)
    category = models.CharField(max_length =200)
    price = models.FloatField()
    discounted_price =  models.FloatField()
    decription = models.TextField(max_length =200)
    image = models.CharField(max_length = 500)

class Order(models.Model):
    items = models.CharField(max_length =1000)
    name = models.CharField(max_length =200)
    email = models.CharField(max_length =200)
    address = models.CharField(max_length =1000)
    city = models.CharField(max_length =200)
    state = models.CharField(max_length =200)
    zipcode = models.CharField(max_length =200)