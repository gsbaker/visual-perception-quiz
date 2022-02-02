from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice


class Command(BaseCommand, ABC):
    help = "Manually create questions"

    def __init__(self):
        super().__init__()
        self.alpha_num_dict = {1: "A", 2: "B", 3: "C", 4: "D"}

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        if options['n'] <= 0:
            raise CommandError("Invalid argument ", options['n'])
        question_id = options['n']
        question = Question.objects.get(pk=question_id)
        for i in range(1, 5):
            choice = Choice()
            choice.choice_text = self.alpha_num_dict.get(i)
            choice.question = question
            choice.save()
