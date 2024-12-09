from django import forms
from django.contrib.auth import  authenticate
from django.core import validators

class UserAuthenticate(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(50)]
    )

    def clean_email(self):
        return self.cleaned_data.get('email').lower()

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            self.user = user
        else:
            raise forms.ValidationError('Invalid email or password')

    def get_user(self):
        return self.user