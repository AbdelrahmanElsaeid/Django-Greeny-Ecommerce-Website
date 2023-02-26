from django.shortcuts import render
from . models import Order, OredrDetail
from django.views.generic import ListView
# Create your views here.




class OrderList(ListView):
    model = Order


    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        
        return queryset