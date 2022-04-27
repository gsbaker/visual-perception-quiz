from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice


class Command(BaseCommand, ABC):
    help = "Prints the correct answers"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        questions = Question.objects.all()
        answers = []
        for question in questions:
            choices = question.choice_set.all()
            for choice in choices:
                if choice.is_correct:
                    answers.append((question.id, choice.choice_text))
        answers.sort(key=lambda tup: tup[0])
        answers = answers[3:]
        print(answers)


