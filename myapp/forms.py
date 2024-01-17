from django import forms
from .models import SignUp  # Import your SignUp model

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['qq','email','username', 'password','confirm_password']  # Add other fields if needed for signup
