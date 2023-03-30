from django.shortcuts import render

# Create your views here.


def Profile(request):
    return render(request, 'accounts/profile.html', {})



def Signup(request):
    return render(request, 'registration/signup.html', {})