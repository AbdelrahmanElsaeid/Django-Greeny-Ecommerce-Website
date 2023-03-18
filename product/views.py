from django.shortcuts import render ,redirect
from django.views.generic import ListView,DetailView
from .models import Product, Brand
from .forms import ProductReviewForm
from django.db.models import Q , F
from django.db.models.aggregates import Avg, Sum, Count, Max 
# Create your views here.


def Product_list_debug(request):

    '''
    - prefetch_related ------> many-to-many
    - select_related   ------> one-to-one     one-to-many

    '''
    #data = Product.objects.all().prefetch_related('brand')
    #data = Product.objects.filter(Q(price__gt=50) & Q(name__contains='avid'))    or & and operations
    #data = Product.objects.filter(sku =F('price'))   # compare two column

    #data = Product.objects.aggregate(Avg('price'))

    data = Product.objects.annotate(new_column=F('price')*1.5)  # add new column and do operations on it from another column


    return render(request, 'product/product_test.html', {'data':data})

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
      