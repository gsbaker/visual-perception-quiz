from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        print(Question.objects.latest('id').id)
