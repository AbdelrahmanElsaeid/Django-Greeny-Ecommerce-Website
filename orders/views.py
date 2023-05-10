from django.shortcuts import render, redirect
from . models import Order, OredrDetail ,Cart,CartDetail,Coupon
from product.models import Product
from django.views.generic import ListView
from settings.models import DeliveryFee
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
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
    total = cart.get_total() + delivery_fee.fee
    code_value=0


    if request.method=='POST':
        coupon_name = request.POST['code']
        coupon = get_object_or_404(Coupon, code = coupon_name)
        today_date = datetime.datetime.today().date()
        if coupon and coupon.quantity > 0:
            if today_date >= coupon.from_date and today_date < coupon.to_date:
                code_value = round(cart.get_total()/100 * coupon.value,2)
                total = cart.get_total() - code_value
                total = total + delivery_fee.fee
                
                html = render_to_string('includes/checkout_result.html',{
                    'cart': cart ,
                    'cart_detail': cart_detail,
                    'delivery_fee': delivery_fee.fee,
                    'total': total,
                    'discount':code_value,
                    'subtotal':cart.get_total()

                })

                return JsonResponse({'result':html})



    return render(request, 'orders/checkout.html',{
        'cart': cart ,
        'cart_detail': cart_detail,
        'delivery_fee': delivery_fee.fee,
        'total': total,
        'discount':code_value,
        'subtotal':cart.get_total()
        })    