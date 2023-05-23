from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, LogoutForm
from .models import Student
from django.utils import timezone
from django.contrib import messages
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
            logout_pincode = form.cleaned_data['logout_pincode']
            if Student.objects.filter(pincode=pincode).exists():
                return render(request, 'main/signup.html', {'form': form, 'error': 'Пин-код уже используется'})
            if Student.objects.filter(logout_pincode=logout_pincode).exists():
                return render(request, 'main/signup.html', {'form': form, 'error': 'Пин-код для выхода уже используется'})
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
                # student.is_visited = True
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



def logout(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout_pincode = form.cleaned_data['logout_pincode']
            student_id = request.session.get('student_id')
            if student_id:
                student = Student.objects.filter(id=student_id, logout_pincode=logout_pincode).first()
                if student:
                    # Clear the session data
                    del request.session['student_id']
                    # Set the logout status to True
                    student.is_exit = True
                    student.save()
                    messages.success(request, 'Вы успешно вышли из системы.')
                    return redirect('login')
                else:
                    form.add_error('logout_pincode', 'Неверный пин-код для выхода')
            else:
                return redirect('login')
    else:
        form = LogoutForm()

    return render(request, 'main/logout.html', {'form': form})





            

