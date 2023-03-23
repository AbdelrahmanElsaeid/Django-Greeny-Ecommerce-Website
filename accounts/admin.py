from django.contrib import admin
from .models import Profile,UserAddress,UserNumbers
# Register your models here.


admin.site.register(Profile)
admin.site.register(UserNumbers)
admin.site.register(UserAddress)