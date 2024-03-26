from django.urls import path
from . import views
app_name = 'shop'


urlpatterns =[
    path('',views.index,name = "index"),
    path('<int:product_id>/',views.detail,name = "detail"),
    path('user_orders/',views.user_orders,name="user_orders"),
    path('view_cart/',views.view_cart,name="view_cart"),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
]