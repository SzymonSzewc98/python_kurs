"""
Main file
"""
class Question:
    def __init__(self, question, answers, idx_of_true):
        self.question = question
        self.answers = answers
        self.true_idx = idx_of_true

    def print_question(self):
        print(self.question, ":")
        print(self.answers)

    def check_if_is_true(self, idx):
        if idx == self.true_idx:
            print("Poprawna odpowiedź!")
            return True
        else:
            print("Niepoprawna odpowiedź!")
            return False

