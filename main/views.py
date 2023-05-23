from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Student
from django.utils import timezone
# Create your views here.


def profile(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    return render(request, 'main/profile.html', {'student': student})


def index(request):
    student = Student.objects.all()
    return render(request, 'main/index.html', {'student': student})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            pincode = form.cleaned_data['pincode']
            if Student.objects.filter(pincode=pincode).exists():
                return render(request, 'registration/register.html', {'form': form, 'error': 'Пин-код уже используется'})
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'main/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pincode = form.cleaned_data['pincode']
            student = Student.objects.filter(pincode=pincode).first()
            if student:
                request.session['student_id'] = student.id
                # Зафиксировать время входа
                student.last_login = timezone.now()
                student.save()
                return redirect('home')
            else:
                form.add_error('pincode', 'Неверный пин-код')
    else:
        form = LoginForm()

    if 'student_id' in request.session:
        return redirect('home')

    return render(request, 'main/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('index')

            

