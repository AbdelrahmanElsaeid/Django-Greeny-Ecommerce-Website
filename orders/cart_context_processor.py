from .models import Cart, CartDetail


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user = request.user, status = 'Inprogress')
        #cart_detail = CartDetail.objects.filter(cart = cart), 'cart_detail': cart_detail
        return {'cart': cart}
    else:
        return {}
