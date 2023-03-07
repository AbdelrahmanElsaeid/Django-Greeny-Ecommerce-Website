from rest_framework import serializers
from .models import Product, Brand, ProductReview



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields = ['id','user','rate','review','data']

class ProductSerializer(serializers.ModelSerializer):
    #brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    reviews = ProductReviewSerializer(source='product_review', many=True )
    class Meta:
        model = Product
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    product = BrandSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'        