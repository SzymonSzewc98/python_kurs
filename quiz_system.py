"""
Main file
"""
def handle_test_question():
    quiz = Quiz()
    quiz.add_question(Question("Jak to jest być skrybą, dobrze, czy niedobrze?",
                               {"a": "Tak", "b": "Nie", "c": "Nie wiem",
                                "d": "Nie ma tak, że dobrze albo że nie dobrze"}, "a"))
    quiz.ask_next_question()

class Question:
    def __init__(self, question, answers, idx_of_true):
        self.question = question
        self.answers = answers
        self.true_idx = idx_of_true

    def print_question(self):
        print(self.question, ":")
        for answer in self.answers:
            print(answer, self.answers[answer])

    def check_if_is_true(self, idx):
        if idx == self.true_idx:
            print("Poprawna odpowiedź!")
            return True
        else:
            print("Niepoprawna odpowiedź!")
            return False

class Quiz:
    def __init__(self):
        self.question_list = []
        self.current_question = 0
    def add_question(self, question):
        self.question_list.append(question)

    def ask_next_question(self):
        self.question_list[self.current_question].print_question()
        self.current_question += 1


handle_test_question()



