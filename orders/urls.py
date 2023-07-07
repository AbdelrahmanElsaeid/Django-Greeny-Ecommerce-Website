from django.urls import path
from .views import OrderList , checkout, add_to_cart, CreateCheckoutSessionView, success_payment
from .api import OrderListApi, CartDetailApi, CreateOrder

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(),name='order_list'),
    path('checkout',checkout,name='checkout'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('create_checkout_session/', CreateCheckoutSessionView.as_view(),name="create_checkout_session"),
    path("payment/success", success_payment),

    #api
    path('api/<str:username>/orders', OrderListApi.as_view()),
    path('api/<str:username>/orders-complete', CreateOrder.as_view()),
    path('api/<str:username>/carts', CartDetailApi.as_view()),

]