from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User, Question


class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()
        self.users = User.objects.all()
        self.correct_responses_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        self.incorrect_responses_dict = self.correct_responses_dict.copy()

    def handle(self, *args, **options):
        print("Full Data Sets:", self.count_full_data_sets())
        print("Q51 Results:", self.inspect_answers(51))
        self.collate_correct_responses()
        print("Correct responses:", self.correct_responses_dict)
        self.collate_incorrect_responses()
        print("Incorrect responses:", self.incorrect_responses_dict)

    def count_full_data_sets(self):
        count = 0
        for user in self.users:
            if len(user.used_question_ids) == 83:
                count += 1
        return count

    def collate_correct_responses_helper(self, question_id, user_choice, set_number):
        question = Question.objects.get(pk=question_id)
        choices = question.choice_set.all()
        for choice in choices:
            if choice.correct:
                if user_choice == choice.choice_text:
                    self.correct_responses_dict[set_number] += 1

    def collate_correct_responses(self):
        for user in self.users:
            if len(user.used_question_ids) == 83:
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

    def collate_incorrect_responses_helper(self, question_id, user_choice, set_number):
        question = Question.objects.get(pk=question_id)
        choices = question.choice_set.all()
        for choice in choices:
            if choice.correct:
                if user_choice != choice.choice_text:
                    self.incorrect_responses_dict[set_number] += 1

    def collate_incorrect_responses(self):
        for user in self.users:
            if len(user.used_question_ids) == 83:
                answers = user.answers
                if len(answers) > 0:
                    for answer in answers:
                        pair = answer.split(",")
                        q_id = int(pair[0])
                        user_choice = pair[1]
                        if q_id in range(4, 14):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 1)
                        elif q_id in range(14, 24):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 2)
                        elif q_id in range(24, 34):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 3)
                        elif q_id in range(34, 44):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 4)
                        elif q_id in range(44, 54):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 5)
                        elif q_id in range(54, 64):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 6)
                        elif q_id in range(64, 74):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 7)
                        elif q_id in range(74, 84):
                            self.collate_incorrect_responses_helper(q_id, user_choice, 8)

    def inspect_answers(self, question_id):
        answers_dict = {"A": 0, "B": 0, "C": 0, "D": 0}
        for user in self.users:
            answers = user.answers
            if len(answers) > 0:
                for answer in answers:
                    pair = answer.split(",")
                    current_question_id = int(pair[0])
                    if current_question_id == question_id:
                        answers_dict[pair[1]] += 1
        return answers_dict
