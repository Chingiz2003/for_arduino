import json
from rest_framework import generics
from .models import *
from .serializers import *
from django.http import HttpResponse
from .forms import RegistrationForm 
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@csrf_exempt
def check_pincode(request):
    if request.method == "POST":
        code = request.POST.get('pincode')

        code_obj = Student.objects.filter(pincode=code).first()

        if code_obj:
            message = "Welcome"
        else:
            message = "Ne welcome"

        return JsonResponse({'message': message})
    
    return  JsonResponse({'error': 'Invalid request method.'})


@csrf_exempt
def check_logout_pincode(request):
    if request.method == "POST":
        code = request.POST.get('logout_pincode')

        code_obj = Student.objects.filter(logout_pincode=code).first()

        if code_obj:
            message = "Welcome to logout"
        else:
            message = "Ne welcome to logout"

        return JsonResponse({'message': message})
    
    return  JsonResponse({'error': 'Invalid request method.'})


class FacultyListAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacSpecListAPIView(generics.ListAPIView):
    queryset = FacSpec.objects.all()
    serializer_class = FacSpecSerializer