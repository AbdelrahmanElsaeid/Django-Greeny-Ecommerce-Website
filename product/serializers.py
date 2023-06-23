from rest_framework import serializers
from .models import Product, Brand, ProductReview, ProductImages
from django.db.models.aggregates import Avg


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
    avg_review = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_price_with_tax(self,product):
        return product.price*1.1

    def get_avg_review(self,product:Product):
        avg = product.product_review.aggregate(myavg=Avg('rate'))
        avg_rate = avg['myavg']
        if avg_rate:
            avg = round(avg_rate,2)
        else:
            avg_rate =0
            avg = avg_rate

        return avg
    def get_reviews_count(self,product:Product):
        review = product.product_review.all().count()
        return review

class ProductDetailSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()
    reviews = ProductReviewSerializer(source='product_review', many=True)
    images = ProductImagesApi(source='product_images', many=True)
    avg_review = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'     


    
    def get_avg_review(self,product:Product):
        avg = product.product_review.aggregate(myavg=Avg('rate'))
        avg_rate = avg['myavg']
        if avg_rate:
            avg = round(avg_rate,2)
        else:
            avg_rate =0
            avg = avg_rate

        return avg
    def get_reviews_count(self,product:Product):
        review = product.product_review.all().count()
        return review    