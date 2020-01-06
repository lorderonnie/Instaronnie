from django import forms
from .models import Photos,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','username')

class Loginform(forms.Form):
    username =forms.CharField(label='Your username',max_length= 50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user= User.objects.filter(username=username)
            if not user:
                raise forms.ValidationError('papapapapapa')
            if not user.check_password(password):
                raise forms.ValidationError('Incoreect password')
        return super(Loginform, self).clean(*args, **kwargs)

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Photos
        exclude = ['user','likes']
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='confirm email')
    username = forms.CharField(label='your username')
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            
        ]
    def clean_password(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        username = self.cleaned_data.get('username')

        if email != email2:
            raise forms.ValidationError('email must match')
        user = User.objects.filter(username = username)
        if user.exists():
            raise forms.ValidationError('This username exists!')
        return username 




        




