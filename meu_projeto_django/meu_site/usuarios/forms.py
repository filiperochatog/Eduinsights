from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class MudarSenhaForm(PasswordChangeForm):
    pass
