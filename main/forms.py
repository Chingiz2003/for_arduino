from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'faculty', 'specialization', 'course', 'pincode']

class LoginForm(forms.Form):
    pincode = forms.CharField(label='Пин-код', max_length=5)


