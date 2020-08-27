from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)
