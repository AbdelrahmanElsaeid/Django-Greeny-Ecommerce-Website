from django.urls import path
from .views import Profile, Signup




app_name='accounts'




urlpatterns = [
    path('profile/',Profile,name='profile'),
    path('signup/',Signup,name='signup'),

]
