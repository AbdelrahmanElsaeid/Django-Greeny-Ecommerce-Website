from django.shortcuts import render ,redirect
from django.views.generic import ListView,DetailView
from .models import Product
from .forms import ProductReviewForm
# Create your views here.




class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product    

def add_review(request,slug):
    product = Product.objects.get(slug = slug)
    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()
    return redirect(f'/products/{product.slug}')        

