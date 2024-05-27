from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)
