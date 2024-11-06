from enum import Enum
"""
Main file
"""
class PrintableEnum(Enum):
    def __str__(self):
        return self.value


class AnswerIndex(PrintableEnum):
    """
    Possible answers values str a, b, c, d
    """
    a = "a"
    b = "b"
    c = "c"
    d = "d"


class CorrectAnswersMessages(PrintableEnum):
    """
    Collection of possible correct answers messages depending on language configuration
    """
    PL = "Poprawna odpowiedź!"
    ENG = "Correct answer!"
    DE = "Eichtige antwort!"


class IncorrectAnswerMessages(PrintableEnum):
    """
    Collection of possible incorrect answers messages depending on language configuration
    """
    PL = "Niepoprawna odpowiedź!"
    ENG = "Incorrect answer!"
    DE = "Falsche antwort!"


class EndMessages(PrintableEnum):
    """
    Collection of possible end messages depending on language configuration
    """
    PL = "KONIEC TESTU"
    ENG = "END OF TEST"
    DE = "ENDE DES TESTS"


class NumberOfQuestionsMessages(PrintableEnum):
    """
    Collection of possible number of questions messages depending on language configuration
    """
    PL = "Ilość pytań: "
    ENG = "Number of questions: "
    DE = "Anzahl der Fragen: "


class NumberOfCorrectAnswersMessages(PrintableEnum):
    """
    Collection of possible number of questions messages depending on language configuration
    """
    PL = "Ilość poprawnych odpowiedzi: "
    ENG = "Number of correct answers: "
    DE = "Anzahl der richtigen Antworten: "


class SummaryMessagesTypes(PrintableEnum):
    """
    Collection of Summary messages types
    """
    END_MESSAGE = 0
    NUMBER_OF_QUESTIONS = 1
    NUMBER_OF_CORRECT_ANSWERS = 2


class Messages(PrintableEnum):
    """
    Collection of message types
    """
    CORRECT_ANSWER = 0
    INCORRECT_ANSWER = 1


class Logger:
    """
    Class implementing message logging logic (facade)
    """
    def print_message(self, message):
        """
        Prints forwarded message, not changing it
        :param message: formatted message
        :return: 
        """
        print(message)


def debug_test_question():
    """
    Debug function for checking quiz functionalities in console
    :return:
    """
    quiz = Quiz()
    quiz.add_question(Question("Jak to jest być skrybą, dobrze, czy niedobrze?",
                               {AnswerIndex.a : "Tak", AnswerIndex.b: "Nie", AnswerIndex.c: "Nie wiem",
                                AnswerIndex.d: "Nie ma tak, że dobrze albo że nie dobrze"}, "d"))
    quiz.ask_next_question()
    quiz.input_answer(input(":"))
    quiz.ask_next_question()

def debug_instructor():
    """
    Debug function for checking intructor functionalities
    :return:
    """
    instructor = Instructor()
    instructor.add_question()
    quiz = instructor.get_quiz()
    quiz.ask_next_question()
    quiz.input_answer(input(":"))
    quiz.ask_next_question()
    quiz.input_answer(input(":"))
    quiz.ask_next_question()
    quiz.input_answer(input(":"))
    quiz.ask_next_question()


class Question:
    """
    Abstraction for question functionalities:
    1. Printing formated question <print_question()>
    2. Validate given answer <check_if_is_true(str idx)>
    3 .Store correct answer (given in <__init__(str question, str{} answers, str idx of true)>)
    """
    def __init__(self, question : str, answers : dict[AnswerIndex, str], index_of_correct_answer : str, logger : Logger = Logger()):
        """
        :param question: str, question to be asked
        :param answers: dictionaries of possible answers dict[AnswerIndex:str]
        :param index_of_correct_answer: AnswerIndex, correct answer (a,b,c,d)
        :param logger: optional parameter
        """
        self.question = question
        self.answers = answers
        self.correct_answer = index_of_correct_answer
        self.logger = logger

    def print_question(self):
        """
        Print formatted question:
        "Question:
        a Anwser a
        b Answer b
        c Answer c
        d Answer d
        :return:
        """
        print(self.question, ":")
        for answer in self.answers:
            print(answer, self.answers[answer])

    def check_if_is_correct(self, idx):
        """
        Check if user passes correct answer
        :param idx: string value of chosen answer (a/b/c/d)
        :return: true if passed value is equal to correct answer index, false if not
        """
        if idx == self.correct_answer:
            self.print_answer_response_message(Messages.CORRECT_ANSWER)
            return True
        else:
            self.print_answer_response_message(Messages.INCORRECT_ANSWER)
            return False

    def print_answer_response_message(self, message_type:Messages):
        """
        Decides which message to print
        :param message_type: type of Message, expected: CORRECT_ANSWER or INCORRECT_ANSWER
        any other will lead to print "wrong message type!"
        :return:
        """
        if message_type == Messages.CORRECT_ANSWER:
            self.logger.print_message(CorrectAnswersMessages.PL)

        elif message_type == Messages.INCORRECT_ANSWER:
            self.logger.print_message(IncorrectAnswerMessages.PL)

        else:
            self.logger.print_message("wrong message type!")


class Quiz:
    """
    Abstraction for Quiz functionalities:
    1. Stores questions
    2. Asks questions in sequence
    3. Collects answer from user
    4. Allows to insert new questions
    5. Calculates test results
    6. Prints test summary
    """
    def __init__(self, logger : Logger = Logger()):
        """
        :param logger: Optional parameter for console logging
        """
        self.question_list: list[Question] = list()
        self.current_question = 0
        self.number_of_correct_answers = 0
        self.logger = logger

    def test_finish(self):
        """
        Test summary
        :return:
        """
        print("KONIEC!")
        print("Ilość pytań: ", len(self.question_list))
        print("Ilość poprawnych odpowiedzi: ", self.number_of_correct_answers)

    def add_question(self, question):
        """
        Allows user (instructor) to insert new question to quiz
        :param question: Question to be inserted (format: "Question: {answer a, answer b, answer c, answer d}, correct answer"
        :return:
        """
        self.question_list.append(question)

    def ask_next_question(self):
        """
        Print next question with answer
        :return:
        """
        if self.current_question < len(self.question_list):
            self.question_list[self.current_question].print_question()
            self.current_question += 1
        else:
            self.test_finish()

    def input_answer(self, index):
        """
        Collect answer from user
        Validate answer
        :param index: User input str
        :return:
        """
        if self.question_list[self.current_question -1].check_if_is_correct(index):
            self.number_of_correct_answers += 1


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


debug_test_question()
debug_instructor()



