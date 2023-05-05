from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Profile, UserNumbers,UserAddress
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import Product,Brand,ProductReview
from orders.models import Order
# Create your views here.

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    numbers = UserNumbers.objects.filter(user=request.user)
    address = UserAddress.objects.filter(user = request.user)
    return render(request, 'accounts/profile.html', {'profile':profile, 'numbers':numbers, 'address': address })



def Signup(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()

            profile = Profile.objects.get(user__username=username)
            send_mail(
                "Activate Your Account",
                f" welcome {username} \n use this code {profile.code} to active your account",
                "pythondeveloper@gmail.com",
                ["email"],
                fail_silently=False,
            )
            return redirect(f"/accounts/{username}/activate")
    else:
        form = SignupForm()    

    return render(request, 'registration/signup.html', {'form':form})


def user_activate(request,username):
    profile =Profile.objects.get(user__username=username)
    if request.method == 'POST':
        code = request.POST['code']
        if code == profile.code:
            profile.code = ' '
            profile.save()
            return redirect('/accounts/login')




    return render(request, 'registration/activate.html',{})


def dashboard(request):
    users = User.objects.count()
    products = Product.objects.count()
    brands = Brand.objects.count()
    reviews = ProductReview.objects.count()
    orders = Order.objects.count()

    recivied_order = Order.objects.filter(status='Recieved').count()
    processed_order = Order.objects.filter(status='Processed').count()
    shipped_order = Order.objects.filter(status='Shipped').count()
    delivered_order = Order.objects.filter(status='Delivered').count()


    return render(request, 'accounts/dashboard.html',{
        'users':users,
        'products':products,
        'brands':brands,
        'reviews':reviews,
        'orders':orders,
        'recivied_order':recivied_order,
        'processed_order':processed_order,
        'shipped_order':shipped_order,
        'delivered_order':delivered_order




    })
