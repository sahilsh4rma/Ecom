from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Order, Cart
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

@login_required
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


def user_orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request,'shop/user_orders.html',{'user_orders':user_orders})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.price = cart_item.quantity * product.price
        cart_item.save()
    else:
        Cart.objects.create(user=request.user, product=product, title=product.title, price=product.price, quantity=1)
    return redirect('shop:index')




def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate total of the cart
    total = sum(item.price for item in cart_items)
    
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items, 'total': total})