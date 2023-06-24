from rest_framework import generics
from .serializers import OrderListSerializer, CartSerializer
from .models import Order ,Cart, CartDetail, OredrDetail
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from product.models import Product




class OrderListApi(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


    def list(self,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        queryset = Order.objects.all().filter(user=user)
        serializer = OrderListSerializer(queryset,many=True)
        return Response(serializer.data)
    

class CreateOrder(generics.GenericAPIView):
    serializer_class = CartSerializer
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart = Cart.objects.get(user=user, status = 'Inprogress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        
        new_order = Order.objects.create(user=user,status = 'Recieved')
        for object in cart_detail:
            OredrDetail.objects.create(
                order = new_order,
                product = object.product,
                quantity = object.quantity,
                price = object.price,
                total = object.total

            )
        cart.status = 'Completed'
        cart.save()
        return Response({'status':'created','message':'order created successfully'})    






class CartDetailApi(generics.GenericAPIView):
    serializer_class = CartSerializer
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status = 'Inprogress') 
        data  = CartSerializer(cart).data
        return Response({'cart':data})  


    def post(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        product = Product.objects.get(id= request.data['product_id'])
        quantity = int(request.data['quantity'])
        cart = Cart.objects.get(user=user, status = 'Inprogress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart, product=product)
        cart_detail.price = product.price
        cart_detail.quantity = quantity
        cart_detail.total = round(quantity*product.price,2)
        cart_detail.save()
        return Response({'status':'created'})

    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        product = Product.objects.get(id= request.data['product_id'])
        cart = Cart.objects.get(user=user, status = 'Inprogress')
        cart_detail = CartDetail.objects.get(cart=cart, product=product)
        cart_detail.delete()
        return Response({'status':'deleted', 'message':'deleted successfully'})