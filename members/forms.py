from django import forms

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
