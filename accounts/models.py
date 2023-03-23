from django.db import models
from django.contrib.auth.models import User
from utils.Generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', null=True, blank=True, default='default.png')
    code = models.CharField(max_length=8,default=generate_code)

@receiver(post_save,sender=User,)
def Create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)

phone_number = (
    ('Primary','Primary'),
    ('Secondary','Secondary')
)

class UserNumbers(models.Model):
    user = models.ForeignKey(User, related_name='user_phones', on_delete=models.CASCADE)
    number = models.CharField(max_length=20 )
    type = models.CharField(max_length=12, choices=phone_number)
    

address_choices = (
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Academy','Academy'),
    ('Other','Other')
)

class UserAddress(models.Model): 
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(max_length=12, choices=address_choices)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    appartment = models.CharField(max_length=20)
    notes = models.CharField(max_length=20)