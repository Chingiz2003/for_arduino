from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'faculty', 'specialization', 'course', 'pincode', 'logout_pincode']

class LoginForm(forms.Form):
    pincode = forms.CharField(label='Пин-код', max_length=5)

class LogoutForm(forms.Form):
    logout_pincode = forms.CharField(label='Пин-код', max_length=6, widget=forms.PasswordInput)




