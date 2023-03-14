from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=20)
    email_us = models.CharField(max_length=20)
    about = models.TextField(max_length=200)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    email = models.TextField(max_length=50)
    address = models.CharField(max_length=200)
    phones = models.TextField(max_length=50)



    def __str__(self):
        return self.name

class DeliveryFee(models.Model):
    fee = models.FloatField()


    def __str__(self):
        return str(self.fee)