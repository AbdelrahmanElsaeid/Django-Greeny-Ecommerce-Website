from django.shortcuts import render
from product.models import Product,Brand, ProductReview

# Create your views here.

def home(request):
    brand = Brand.objects.all()
    sale = Product.objects.filter(flag='Sale')[:10]
    feature = Product.objects.filter(flag='Feature')[:6]
    new = Product.objects.filter(flag='New')[:6]
    reviews = ProductReview.objects.all()


    return render(request, 'settings/home.html', {'brand': brand, 'sale': sale, 'feature': feature, 'new': new, 'reviews': reviews})
