from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice


class Command(BaseCommand, ABC):
    help = "Rename choices to A, B, C, D"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        questions = Question.objects.all()
        for question in questions:
            choices = question.choice_set.all()
            for choice in choices:
                choice.choice_text = choice.choice_text[-1]
                choice.save()
