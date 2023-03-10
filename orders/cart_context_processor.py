from .models import Cart, CartDetail


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user = request.user, status = 'Inprogress')
        cart_detail = CartDetail.objects.filter(cart = cart)
        return {'cart': cart , 'cart_detail': cart_detail}
    else:
        return {}
