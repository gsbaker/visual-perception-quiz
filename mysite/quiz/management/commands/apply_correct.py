from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice

import csv
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()
        self.answer_dict = {4: "B", 5: "C", 6: "A", 7: "D", 8: "C", 9: "B", 10: "C", 11: "D", 12: "B", 13: "A",
                            14: "D", 15: "C", 16: "B", 17: "C", 18: "D", 19: "D", 20: "D"}

    def handle(self, *args, **options):
        questions = Question.objects.all()
        for question in questions:
            is_clear_answer = question.image_number not in [1, 2, 3, 21, 22, 23]
            if is_clear_answer:
                choices = question.choice_set.all()
                correct_answer = self.answer_dict[question.image_number]
                for choice in choices:
                    if choice.choice_text == correct_answer:
                        choice.is_correct = True
                    else:
                        choice.is_correct = False
                    choice.save()
            else:
                if question.image_number == 21:
                    choices = question.choice_set.all()
                    for choice in choices:
                        if choice.choice_text in ["B", "D"]:
                            choice.is_correct = True
                        else:
                            choice.is_correct = False
                        choice.save()
                elif question.image_number == 22:
                    choices = question.choice_set.all()
                    for choice in choices:
                        if choice.choice_text in ["A", "B", "C"]:
                            choice.is_correct = True
                        else:
                            choice.is_correct = False
                        choice.save()
                elif question.image_number == 23:
                    choices = question.choice_set.all()
                    for choice in choices:
                        choice.is_correct = True
                        choice.save()
