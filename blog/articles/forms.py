from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

user_model = get_user_model()


class UserRegister(UserCreationForm):
    username = forms.CharField(max_length=150,
                               label="Username",
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "autocomplete": "off",
                                                             "placeholder": "only chars, nums and . - _ +"}))
    email = forms.EmailField(required=True,
                             label="Email",
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "autocomplete": "off", }))
    password1 = forms.CharField(min_length=8,
                                label="Password",
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "autocomplete": "off",
                                                                  "placeholder": "min-length 8"}))
    password2 = forms.CharField(min_length=8,
                                label="Password confirm",
                                widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                  "autocomplete": "off",
                                                                  "placeholder": "repeat your password"}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

    class Meta:
        model = user_model
        fields = ("username", "email")


class UserLogin(AuthenticationForm):
    username = forms.CharField(max_length=150,
                               label="Username",
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "autocomplete": "off",
                                                             "placeholder": "Enter your username"}))
    password = forms.CharField(min_length=8,
                               label="Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 "autocomplete": "off",
                                                                 "placeholder": "Enter your password"}))


