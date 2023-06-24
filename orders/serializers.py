from rest_framework import serializers
from .models import Order, OredrDetail, Cart,CartDetail





class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OredrDetail
        fields = ['product','quantity','price']


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    order_detail = OrderDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = ['product','quantity','price','total'] 

class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many = True)
    user = serializers.StringRelatedField()
    class Meta:
        model =  Cart
        fields = '__all__'


              