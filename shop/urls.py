from django.urls import path
from . import views
app_name = 'shop'


urlpatterns =[
    path('',views.index,name = "index"),
    path('<int:product_id>/',views.detail,name = "detail"),
    path('checkout/',views.checkout,name="checkout"),
    path('user_orders/',views.user_orders,name="user_orders"),
]