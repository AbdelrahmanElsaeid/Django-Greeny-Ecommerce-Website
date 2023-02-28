from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(OredrDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Coupon)