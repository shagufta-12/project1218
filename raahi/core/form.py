from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Password again", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email=forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields={'username', 'email'}
        widgets={'username' :forms.TextInput(attrs={'class':'form-control'})}

class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password=forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )
class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class':'form-control'})
    )

    new_password1 = forms.CharField(
        label="New password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class':'form-control'})
    )

    new_password2 = forms.CharField(
        label="Old password Again",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class':'form-control'})
    )
