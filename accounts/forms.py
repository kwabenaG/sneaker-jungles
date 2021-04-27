# accounts.forms

from django.contrib.auth.forms import forms
from .models import CustomUser, UserProfile


# overrides the all-auth signup forms
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput())

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget = forms.TextInput(attrs="{}")

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    # def signup(self, request, user, *args, **kwargs):
    #     user.password1 = user.cleaned_data['password1']
    #     user.password2 = user.cleaned_data['password2']
    #     user.save()
    #     return user