from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    product_objects =Product.objects.all()
    product_name = request.GET.get("item_name")
    if product_name != "" and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name )
    paginator = Paginator(product_objects,1)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects' : product_objects})

def detail(request, product_id):
    product =  Product.objects.get(pk = product_id)
    return render(request,'shop/detail.html',{'product' : product})

def checkout(request):
    if request.method == "POST":
        items =request.POST.get("items","")
        name =request.POST.get("name","")
        email =request.POST.get("email","")
        address =request.POST.get("address","")
        city =request.POST.get("city","")
        state =request.POST.get("state","")
        zipcode =request.POST.get("zipcode","")
        total =request.POST.get("total","")
        order = Order(items = items, name = name ,email = email ,address = address ,city = city ,state = state ,zipcode = zipcode, total = total)
        order.save()

    return render(request,'shop/checkout.html')