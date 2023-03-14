from django.shortcuts import render, redirect
from . models import Order, OredrDetail ,Cart,CartDetail
from product.models import Product
from django.views.generic import ListView
from settings.models import DeliveryFee
from django.contrib.auth.decorators import login_required
# Create your views here.




class OrderList(ListView):
    model = Order


    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        
        return queryset
    

def add_to_cart(request):
    if request.method=='POST':
        product_id = request.POST['productid']
        quantity = request.POST['quantity']
        
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user, status='Inprogress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)

        cart_detail.quantiy=int(quantity)
        cart_detail.price=product.price
        cart_detail.total=int(quantity)*product.price
        cart_detail.save()
    return redirect(f'/products/{product.slug}')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last()
    total = cart.get_total()

    return render(request, 'orders/checkout.html',{'cart': cart , 'cart_detail': cart_detail, 'delivery_fee': delivery_fee, 'total': total})    