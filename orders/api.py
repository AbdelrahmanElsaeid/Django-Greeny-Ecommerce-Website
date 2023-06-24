from rest_framework import generics
from .serializers import OrderListSerializer
from .models import Order
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
    