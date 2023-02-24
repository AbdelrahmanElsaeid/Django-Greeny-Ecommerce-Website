from django.shortcuts import render ,redirect
from django.views.generic import ListView,DetailView
from .models import Product, Brand
from .forms import ProductReviewForm
# Create your views here.




class ProductList(ListView):
    model = Product
    paginate_by = 50

    extra_context = {'all_count': Product.objects.all().count()}



class ProductDetail(DetailView):
    model = Product   

    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context["related_products"] = Product.objects.filter(brand=product.brand)[:10]
        return context
     

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



class BrandList(ListView):
    model = Brand
    paginate_by = 50
    extra_context = {'add_count': Brand.objects.all().count()}




class BrandDetail(ListView):
    model = Product
    paginate_by = 50
    template_name = 'product/brand_detail.html'  

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
      