from django.contrib import admin
from django.urls import path
from .views import *
from django.http import HttpResponse

urlpatterns = [
    path('', index, name='home'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('signup', register, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile', profile, name='profile'),
]
