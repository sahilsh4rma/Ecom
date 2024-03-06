from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    product_objects =Products.objects.all()
    product_name = request.GET.get("item_name")
    if product_name != "" and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name )
    return render(request,'shop/index.html',{'product_objects' : product_objects})