import os

from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    used_question_ids = ArrayField(models.IntegerField(), default=list)
    answers = ArrayField(models.CharField(max_length=200), default=list)

    def __str__(self):
        return "User #" + str(self.id)


class Question(models.Model):
    image_number = models.IntegerField(default=0)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + '. ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)
    crowd_percentage = models.IntegerField(default=0)

    def __str__(self):
        if os.environ['DJANGO_SETTINGS_MODULE'] == 'mysite.settings.dev':
            return str(self.question.id) + '.' + str(self.choice_text)
        return str(self.choice_text)


class QuestionChoices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choices = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})
