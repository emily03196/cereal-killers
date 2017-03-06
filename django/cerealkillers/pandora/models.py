from django.db import models
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class MCChoice(models.Model):
    queston = models.ForeignKey(Question, on_delete=models.CASCADE)
    mcchoice_text = models.CharField(max_length=500) 
    def __str__(self):
        return self.mcchoice_text


# class DropdownChoice(models.Model):
# https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield