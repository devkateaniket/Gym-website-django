from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer


class CustomerForm(forms.ModelForm):
    join_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Customer
        fields = [
            'full_name',
            'email',
            'phone',
            'age',
            'gender',
            'address',
            'plan_choice',
            'join_date',
        ]


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
