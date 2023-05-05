from django.urls import path
from .views import Profile, Signup, user_activate




app_name='accounts'




urlpatterns = [
    path('<str:username>/activate', user_activate, name = 'user_activate'),
    path('profile/',Profile,name='profile'),
    path('signup/',Signup,name='signup'),

]
