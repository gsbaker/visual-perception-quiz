from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        users = User.objects.all()
        answers_dict = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

        for user in users:
            answers = user.answers
            if len(answers) > 0:
                for answer in answers:
                    pair = answer.split(",")
                    q_id = int(pair[0])
                    if q_id == 52:
                        answers_dict[pair[1]] += 1
        print(answers_dict)

