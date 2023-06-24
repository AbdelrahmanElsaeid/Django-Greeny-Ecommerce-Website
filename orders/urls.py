from django.urls import path
from .views import OrderList , checkout, add_to_cart
from .api import OrderListApi

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(),name='order_list'),
    path('checkout',checkout,name='checkout'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),


    #api
    path('api/<str:username>/orders', OrderListApi.as_view()),

]