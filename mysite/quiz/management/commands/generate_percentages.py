from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, Choice

import csv
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand, ABC):
    help = "Generate percentages based on CSV file"

    def handle(self, *args, **options):
        url = staticfiles_storage.path("quiz/percentages.csv")
        with open(url) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                # ex row: ['1', '0', '100', '0', '0']
                question_id = row[0]
                percentages = row[1:]
                question = Question.objects.get(pk=int(question_id))
                choices = question.choice_set.order_by('choice_text')
                index = 0
                for choice in choices:
                    choice.crowd_percentage = int(percentages[index])
                    choice.save()
                    index += 1

                question.save()
