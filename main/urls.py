from django.contrib import admin
from django.urls import path
from .views import *
from django.http import HttpResponse
from rest_framework.authtoken import views as drf_views
from main import api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', index, name='home'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('signup', register, name='signup'),
    path('logout/', logout, name='logout'),
    path('profile', profile, name='profile'),

    #api urls
    path('api/student/', api_views.StudentListAPIView.as_view(), name='get_student'),
    path('api/check_pincode/', api_views.check_pincode, name='check_pincode'),
    path('api/check_logout_pincode/', api_views.check_logout_pincode, name='check_logout_pincode'),
]
