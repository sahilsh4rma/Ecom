from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length =200)
    category = models.CharField(max_length =200)
    price = models.FloatField()
    discounted_price =  models.FloatField()
    decription = models.TextField(max_length =200)
    image = models.CharField(max_length = 500)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , default = 1)
    items = models.CharField(max_length =1000)
    name = models.CharField(max_length =200)
    email = models.CharField(max_length =200)
    address = models.CharField(max_length =1000)
    city = models.CharField(max_length =200)
    state = models.CharField(max_length =200)
    zipcode = models.CharField(max_length =200)
    total = models.FloatField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.pk} - {self.order_datetime.strftime('%Y-%m-%d %H:%M:%S')}"