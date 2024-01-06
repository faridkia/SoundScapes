from django import  forms
from .models import User
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id':'login',
        'class':'fadeIn second',
        'placeholder':'Username or Phone number',
    }), required=True, label=False)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'id': 'password',
        'class': 'fadeIn third',
        'placeholder': 'Password',
    }), required=True, label=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Check if the username exists
        if not User.objects.filter(Q(username=username) | Q(phone=username)).exists():
            raise forms.ValidationError({'username': 'Wrong username/password'})

        # Example: Password should contain at least 8 characters
        if len(password) < 8:
            raise forms.ValidationError({'password': 'Password should be at least 8 characters long.'})

        # Return the cleaned data
        return cleaned_data

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'id': 'password',
        'class': 'fadeIn fourth',
        'placeholder': 'Password',
    }), required=True, label=False)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'id': 'password2',
        'class': 'fadeIn fifth',
        'placeholder': 'Confirm Password',
    }), required=True, label=False)
    class Meta:
        model = User
        fields = ['username','first_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'class': 'fadeIn second',
                'placeholder': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'id': 'first_name',
                'class': 'fadeIn third',
                'placeholder': 'Firstname',
            }),
        }
        labels = {
            'username' : '',
            'first_name' : ''
        }
        help_texts = {
            'username' : ''
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords are not same!')
        if len(cd['password1']) < 8 :
            raise forms.ValidationError('Password should be at least 8 characters long.')
        return cd['password2']

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254,label='', widget=forms.EmailInput(attrs={
        'class': 'fadeIn second',
        'placeholder': 'Email',
        "autocomplete": "email",
        'id': 'id_email'
    }))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'fadeIn first',
        'id' : 'password1',
        'placeholder': 'New password',
        'type': 'password',
        'name': 'new_password1'
    }))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'FadeIn second',
        'id': 'password2',
        'placeholder': 'Confirm new password',
        'type': 'password',
        'name': 'new_password2'
    }))