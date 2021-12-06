from django import forms

from accounts.models import CustomUser


class CustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'surname', 'email']