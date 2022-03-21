from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User, Question


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()
        self.users = User.objects.all()
        self.set_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    def handle(self, *args, **options):
        self.same_length_answers()
        self.collate_correct_responses()
        print(self.set_dict)

    def collate_correct_responses_helper(self, question_id, user_choice, set_number):
        question = Question.objects.get(pk=question_id)
        choices = question.choice_set.all()
        for choice in choices:
            if choice.correct:
                if user_choice == choice.choice_text:
                    self.set_dict[set_number] += 1

    def collate_correct_responses(self):
        for user in self.users:
            answers = user.answers
            if len(answers) > 0:
                for answer in answers:
                    pair = answer.split(",")
                    q_id = int(pair[0])
                    user_choice = pair[1]
                    if q_id in range(4, 14):
                        self.collate_correct_responses_helper(q_id, user_choice, 1)
                    elif q_id in range(14, 24):
                        self.collate_correct_responses_helper(q_id, user_choice, 2)
                    elif q_id in range(24, 34):
                        self.collate_correct_responses_helper(q_id, user_choice, 3)
                    elif q_id in range(34, 44):
                        self.collate_correct_responses_helper(q_id, user_choice, 4)
                    elif q_id in range(44, 54):
                        self.collate_correct_responses_helper(q_id, user_choice, 5)
                    elif q_id in range(54, 64):
                        self.collate_correct_responses_helper(q_id, user_choice, 6)
                    elif q_id in range(64, 74):
                        self.collate_correct_responses_helper(q_id, user_choice, 7)
                    elif q_id in range(74, 84):
                        self.collate_correct_responses_helper(q_id, user_choice, 8)

    def same_length_answers(self):
        answers_dict = {"A": 0, "B": 0, "C": 0, "D": 0}
        answers_51 = answers_dict.copy()
        answers_52 = answers_dict.copy()
        answers_53 = answers_dict.copy()
        answers_61 = answers_dict.copy()
        answers_62 = answers_dict.copy()
        answers_63 = answers_dict.copy()
        for user in self.users:
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
