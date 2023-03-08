from rest_framework import serializers
from .models import Product, Brand, ProductReview, ProductImages



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields = ['id','user','rate','review','data']


class BrandDetailSerializer(serializers.ModelSerializer):
    product = BrandSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'        


class ProductImagesApi(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']   

class ProductSerializer(serializers.ModelSerializer):
    
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_price_with_tax(self,product):
        return product.price*1.1    

class ProductDetailSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()
    reviews = ProductReviewSerializer(source='product_review', many=True)
    images = ProductImagesApi(source='product_images', many=True)
    class Meta:
        model = Product
        fields = '__all__'     