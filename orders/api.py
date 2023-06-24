from rest_framework import generics
from .serializers import OrderListSerializer, CartSerializer
from .models import Order ,Cart, CartDetail
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User




class OrderListApi(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


    def list(self,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        queryset = Order.objects.all().filter(user=user)
        serializer = OrderListSerializer(queryset,many=True)
        return Response(serializer.data)
    

class CartDetailApi(generics.GenericAPIView):
    serializer_class = CartSerializer
    def get(self,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status = 'Inprogress') 
        data  = CartSerializer(cart).data
        return Response({'cart':data})  


    def post(self,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        pass 

    def delete(self,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        pass 