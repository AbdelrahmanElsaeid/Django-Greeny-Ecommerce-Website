from django.urls import path
from .views import profile, Signup, user_activate,dashboard




app_name='accounts'




urlpatterns = [
    path('<str:username>/activate', user_activate, name = 'user_activate'),
    path('dashboard',dashboard,name='dashboard'),
    path('profile/',profile,name='profile'),
    path('signup/',Signup,name='signup'),

]
