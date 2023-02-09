from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
FLAG_TYPES = (
    ('New' , 'New'),
    ('Feature' , 'Feature'),
    ('Sale' , 'Sale'),
)



class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    sku = models.IntegerField()
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=20000)
    flag = models.CharField(choices= FLAG_TYPES, max_length=10)
    brand = models.ForeignKey('Brand',related_name='product_brand' , on_delete=models.SET_NULL, null=True,blank=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True)    

    def __str__(self):
        return self.name




class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')
    slug = models.SlugField(null=True, blank=True)    

    def __str__(self):
        return str(self.name)


class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review', on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.TextField(max_length=400) 
    data = models.DateTimeField(default=timezone.now)   

    def __str__(self):
        return str(self.user)

class ProductImages(models.Model):
    Product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')


    def __str__(self):
        return str(self.product)