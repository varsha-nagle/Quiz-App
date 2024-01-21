from django.forms import ModelForm
from django.db import models


# Create your models here.
class user(ModelForm):
    fields = ['username', 'email']


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
