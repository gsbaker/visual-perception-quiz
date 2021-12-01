from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice


class Command(BaseCommand, ABC):
    help = "Manually create questions"

    def __init__(self):
        super().__init__()
        self.alpha_num_dict = {1: "A", 2: "B", 3: "C", 4: "D"}
        self.question_text = "Which is the tallest line?"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        if options['n'] <= 0:
            raise CommandError("Invalid argument ", options['n'])

        for _ in range(options['n']):
            question = Question()
            question.question_text = self.question_text
            question.save()

            for i in range(1, 5):
                choice = Choice()
                choice.choice_text = "Line {}".format(self.alpha_num_dict.get(i))
                choice.question = question
                choice.save()
