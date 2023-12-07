from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Va rugam folositi alta adresa de email')
        return email

class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Parolele introduse nu coincid.",
        'password_common': "Parola nu poate fi una comună.",
    }