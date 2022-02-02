from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    def __str__(self):
        return "User #" + str(self.id)

    def get_incorrect_choices(self):
        incorrect_choices = []
        for incorrect_choice in self.incorrectchoice_set.all():
            question_id = str(incorrect_choice.question.id)
            choice = str(incorrect_choice.choice)
            formatted_string = question_id + ": " + choice
            incorrect_choices.append(formatted_string)
        return incorrect_choices


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ". " + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)


class IncorrectChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choices = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})
