from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username",'autofocus': 'autofocus','required': 'required'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password",'required': 'required'}),label='')

class MarketUserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Name",'autofocus': 'autofocus','required': 'required'}),label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control","placeholder":"Email",'required': 'required'}),label='')
    password = forms.CharField(widget=forms.TextInput(attrs={"type" : "password", "class":"form-control","placeholder":"Password",'required': 'required'}),label='')
