from quiz import*


class Instructor:
    """
    Abstraction for Instructor functionalities:
    1. Creates quizes
    2. Adds questions to quizes

    """
    def __init__(self):
        self.quiz = Quiz()
        questions = [
                        Question("Ile to 2 + 2", {AnswerIndex.a : "5", AnswerIndex.b : "5", AnswerIndex.c : "4", AnswerIndex.d : "5"}, "c"),
                        Question("Ile to 2 + 3", {AnswerIndex.a: "5", AnswerIndex.b: "2", AnswerIndex.c: "4", AnswerIndex.d: "1"}, "a")
                    ]
        for question in questions:
            self.quiz.add_question(question)

    def add_question(self):
        """
        Allows adding questions from console
        1. Asks for question
        2. Asks for following answers
        3. Asks for correct answer
        :return:
        """
        self.quiz.add_question(
                                    Question(input("Podaj pytanie"),
                                        {AnswerIndex.a : input("Podaj odpowiedz a:"), AnswerIndex.b : input("Podaj odpowiedz b:"),
                                                AnswerIndex.c : input("Podaj odpowiedz c:"), AnswerIndex.d : input("Podaj odpowiedz d:") },
                                                input("Podaj poprawną odpowiedź:")
                                             )
                               )

    def get_quiz(self):
        return self.quiz