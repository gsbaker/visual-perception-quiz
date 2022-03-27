from abc import ABC

from django.core.management.base import BaseCommand, CommandError
from quiz.models import User, Question


# tests on prod data

class Command(BaseCommand, ABC):
    help = "Counts the number of questions"

    def __init__(self):
        super().__init__()
        self.users = User.objects.all()

    def handle(self, *args, **options):
        print("Full Data Sets:", self.count_full_data_sets())
        print("Q51 Results:", self.inspect_answers(51))
        print("Crowd percentages (1) seem ok:", self.test_crowd_correct(1))
        answers_dicts = self.analyse_answers()
        print("Correct answers:", answers_dicts[0])
        print("Incorrect answers", answers_dicts[1])
        print("Agree with crowd answers", answers_dicts[2])

    def count_full_data_sets(self):
        count = 0
        for user in self.users:
            if len(user.used_question_ids) == 83:
                count += 1
        return count

    @staticmethod
    def count_correct_answers(answers, section):
        count = 0
        n = (10 * section) - 6
        for i in range(n, n + 10):
            question = Question.objects.get(pk=i)
            choices = question.choice_set.all()
            for choice in choices:
                if choice.correct:
                    if choice.choice_text == answers[i-1][1]:
                        count += 1
        return count

    @staticmethod
    def count_incorrect_answers(answers, section):
        count = 0
        n = (10 * section) - 6
        for i in range(n, n + 10):
            question = Question.objects.get(pk=i)
            choices = question.choice_set.all()
            for choice in choices:
                if choice.correct:
                    if choice.choice_text != answers[i - 1][1]:
                        count += 1
        return count

    @staticmethod
    def count_agree_with_crowd_answers(answers, section):
        count = 0
        n = (10 * section) - 6
        for i in range(n, n + 10):
            question = Question.objects.get(pk=i)
            choices = question.choice_set.all()
            crowd_choice = choices[0]
            for choice in choices:
                if choice.percentage > crowd_choice.percentage:
                    crowd_choice = choice
            if crowd_choice.choice_text == answers[i - 1][1]:
                count += 1
        return count

    def analyse_answers(self):
        responses_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        correct_answers = responses_dict.copy()
        incorrect_answers = responses_dict.copy()
        agree_with_crowd_answers = responses_dict.copy()
        for user in self.users:
            if len(user.used_question_ids) == 83:
                unordered_answers = []
                for answer in user.answers:
                    question_choice_pair = answer.split(",")
                    answer_question_id = int(question_choice_pair[0])
                    answer_choice = question_choice_pair[1]
                    unordered_answers.append((answer_question_id, answer_choice))
                ordered_answers = sorted(unordered_answers, key=lambda tup: tup[0])
                for i in range(1, 9):
                    correct_answers[i] += self.count_correct_answers(ordered_answers, i)
                    incorrect_answers[i] += self.count_incorrect_answers(ordered_answers, i)
                    agree_with_crowd_answers[i] += self.count_agree_with_crowd_answers(ordered_answers, i)
        return correct_answers, incorrect_answers, agree_with_crowd_answers

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

    @staticmethod
    def test_crowd_correct(section):
        n = (10 * section) - 6
        for i in range(n, n + 10):
            question = Question.objects.get(pk=i)
            choices = question.choice_set.all()
            crowd_choice = choices[0]
            for choice in choices:
                if choice.percentage > crowd_choice.percentage:
                    crowd_choice = choice
            for choice in choices:
                if choice.correct:
                    if crowd_choice.choice_text != choice.choice_text:
                        return False, str(choice)
            return True