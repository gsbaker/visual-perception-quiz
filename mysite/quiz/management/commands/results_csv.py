from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User

import csv
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand, ABC):
    help = "Creates a CSV of results"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        users = User.objects.all()
        url = staticfiles_storage.path("quiz/results.csv")
        with open(url, 'w') as file:
            writer = csv.writer(file)
            for user in users:
                answers = user.answers
                if len(answers) > 0:
                    writer.writerow(answers)

