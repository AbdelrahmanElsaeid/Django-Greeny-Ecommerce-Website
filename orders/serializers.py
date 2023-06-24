from rest_framework import serializers
from .models import Order, OredrDetail





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