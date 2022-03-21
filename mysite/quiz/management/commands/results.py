from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        users = User.objects.all()
        answers_51 = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

        answers_52 = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

        answers_53 = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

        answers_61 = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
         }

        answers_62 = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
         }

        answers_63 = {
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
                    if q_id == 51:
                        answers_51[pair[1]] += 1
                    elif q_id == 52:
                        answers_52[pair[1]] += 1
                    elif q_id == 53:
                        answers_53[pair[1]] += 1
                    elif q_id == 61:
                        answers_61[pair[1]] += 1
                    elif q_id == 62:
                        answers_62[pair[1]] += 1
                    elif q_id == 63:
                        answers_63[pair[1]] += 1

        print(51, answers_51)
        print(52, answers_52)
        print(53, answers_53)
        print(61, answers_61)
        print(62, answers_62)
        print(63, answers_63)

