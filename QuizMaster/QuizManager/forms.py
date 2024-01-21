from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class addQuestionform(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
