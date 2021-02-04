from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CreateNewOrder, QrCodeSave


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username', 'password1', 'password2'] 


class ProfileUpdateForm(forms.ModelForm):
    patronymic = forms.CharField()
    phone = forms.CharField()

    class Meta:
        model = Profile
        fields = ['patronymic', 'phone']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CreateNewOrderForm(forms.Form):
    method_of_obtaining = forms.CharField()
    payment_method = forms.CharField()
    contact = forms.CharField()
    address = forms.CharField()


class Check(forms.Form):
    сheckbox = forms.BooleanField()


class UploadFileForm(forms.Form):
    image = forms.ImageField()
    id_product = forms.CharField()
    count = forms.CharField()
