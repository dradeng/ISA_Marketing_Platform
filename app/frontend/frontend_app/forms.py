from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Email",'autofocus': 'autofocus','required': 'required'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password",'required': 'required'}),label='')

class MarketUserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Name",'autofocus': 'autofocus','required': 'required'}),label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control","placeholder":"Email",'required': 'required'}),label='')
    password = forms.CharField(widget=forms.TextInput(attrs={"type" : "password", "class":"form-control","placeholder":"Password",'required': 'required'}),label='')

class adCreateForm(forms.Form):
    site_title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"title",'autofocus': 'autofocus','required': 'required'}),label='')
    url = forms.URLField(widget=forms.URLInput(attrs={"class":"form-control","placeholder":"url",'autofocus': 'autofocus','required': 'required'}),label='')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"10",'autofocus': 'autofocus','required': 'required'}),label='')
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"10",'autofocus': 'autofocus','required': 'required'}),label='')
