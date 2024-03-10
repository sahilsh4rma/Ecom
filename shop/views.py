from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    product_objects =Products.objects.all()
    product_name = request.GET.get("item_name")
    if product_name != "" and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name )
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects' : product_objects})

def detail(request, product_id):
    product =  Products.objects.get(pk = product_id)
    return render(request,'shop/detail.html',{'product' : product})

def checkout(request):
    return render(request,'shop/checkout.html')