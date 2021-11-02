from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    score = models.IntegerField(default=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ". " + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.choice_text)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choices = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})
