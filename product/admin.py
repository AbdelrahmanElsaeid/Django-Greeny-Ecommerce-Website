from django.contrib import admin
from .models import Product, ProductImages, ProductReview, Brand
# Register your models here.



class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]





admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Brand)