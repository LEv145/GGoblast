from phonenumber_field.formfields import PhoneNumberField
from django import forms

from .models import ProfileInterest


class RegisterForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    interests = forms.ModelMultipleChoiceField(queryset=ProfileInterest.objects)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    telephone_number = PhoneNumberField(required=False)
    email = forms.EmailField(required=False)
    image = forms.ImageField(required=False)
