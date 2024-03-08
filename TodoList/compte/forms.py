from django import forms
from django.contrib.auth.models import User



class CreateUserForm(forms.ModelForm):

    class Meta:
        model= User

        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer login'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer nom categorie'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }
