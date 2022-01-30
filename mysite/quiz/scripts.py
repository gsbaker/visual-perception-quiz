def find_high_score(scores):
    high_score = 0
    for score in scores:
        if score > high_score:
            high_score = score
    return high_score


def get_sorted_choice_set(question):
    choice_set = question.choice_set.all()
    print(choice_set)