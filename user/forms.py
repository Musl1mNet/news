from django import forms
from news.validators import PhoneValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.core.validators import ValidationError
from .models import User


class RegestrationForm(forms.ModelForm):

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[MinLengthValidator(6)])
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[MinLengthValidator(6)])

    class Meta():
        model = User
        fields = ['username', 'phone', 'password', 'confirm']




    # username = forms.CharField(max_length=20, validators=[UnicodeUsernameValidator()])
    # phone = forms.CharField(max_length=14, validators=[PhoneValidator()])
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[MinLengthValidator(7)])
    # confirm = forms.CharField(max_length=50, widget=forms.PasswordInput(),validators=[MinLengthValidator(7)])

    # def clean_username(self):
    #     if User.objects.filter(username = self.cleaned_data.get('username')).exists():
    #         raise ValidationError("Ushbu nickname band!")
    #     return self.cleaned_data['username']
    #
    # def clean_phone(self):
    #     if User.objects.filter(phone = self.cleaned_data.get('phone')).exists():
    #         raise ValidationError("Ushbu telefon raqam band!")
    #     return self.cleaned_data['phone']
    #
    # def clean_confirm(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['confirm']:
    #         raise ValidationError("Parolni qayta terishda xatolik!")
    #     return self.cleaned_data['confirm']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)

    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "phone", "first_name", "last_name", "email"]
