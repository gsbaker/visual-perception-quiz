from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice

import csv
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        url = staticfiles_storage.path("quiz/image_numbers.csv")
        with open(url) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                question_id = int(row[0])
                image_number = int(row[1])
                try:
                    question = Question.objects.get(pk=question_id)
                    question.image_number = image_number
                    question.save()
                except:
                    print(question_id)

