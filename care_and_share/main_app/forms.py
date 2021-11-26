from django import forms

from accounts.models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'surname', 'email', 'password_1', 'password_2']