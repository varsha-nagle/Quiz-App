from django.forms import ModelForm


# Create your models here.
class user(ModelForm):
    field = ['username', 'email']

