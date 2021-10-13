from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# registro de usuario
class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta:
      model = User
      fields = ['username', 'email', 'first_name','last_name']