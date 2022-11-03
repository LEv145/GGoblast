from phonenumber_field.formfields import PhoneNumberField
from django import forms

from .models import Interest, Profile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    interests = forms.ModelChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    telephone_number = PhoneNumberField(required=False)

    class Meta:
        model = Profile
        fields = [
            "name",
            "surname",
            "password",
            "confirm_password",
            "interests",
            "telephone_number",
            "email",
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароль и подтверждение праоля не совпадают",
            )
