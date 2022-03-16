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
                percentages = row[1:]
                total = 0
                for i in range(len(percentages)):
                    total += int(percentages[i])
                if total != 100:
                    print("Fail", str(total), row[0])
