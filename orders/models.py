from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from utils.Generate_code import generate_code
# Create your models here.



CART_STATUS = (
    ('Inprogress' , 'Inprogress'),
    ('Completed' , 'Completed'),
   
    )

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.SET_NULL,null=True, blank=True)    
    status = models.CharField(max_length=12 , choices=CART_STATUS)


    def __str__(self):
        return str(self.user)



class CartDetail(models.Model):
    order = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_product', on_delete= models.SET_NULL, null=True,blank=True)
    quantiy = models.IntegerField()
    price = models.FloatField
    total = models.FloatField()



    def __str__(self):
        return str(self.order)




ORDER_STATUS = (
    ('Recieved' , 'Recieved'),
    ('Processed' , 'Processed'),
    ('Shipped' , 'Shipped'),
    ('Delivered' , 'Delivered')
    )

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.SET_NULL,null=True, blank=True)
    code = models.CharField(max_length=10, default=generate_code)
    status = models.CharField(max_length=12 , choices=ORDER_STATUS)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code



class OredrDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_product', on_delete= models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()




    def __str__(self):
        return str(self.order)
    



class Coupon(models.Model):
    code = models.CharField(max_length=10)
    value = models.FloatField()
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coupon/')

    def __str__(self):
        return self.code   