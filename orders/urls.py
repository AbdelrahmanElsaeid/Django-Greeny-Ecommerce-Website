from django.urls import path
from .views import OrderList , checkout

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(),name='order_list'),
    path('checkout', checkout,name='checkout'),

]