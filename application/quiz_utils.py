from enum import Enum


__all__ = [
        'AnswerIndex', 'CorrectAnswersMessages',
        'IncorrectAnswerMessages', 'EndMessages',
        'NumberOfQuestionsMessages', 'NumberOfCorrectAnswersMessages',
        'SummaryMessagesTypes', 'Messages',
        'Logger',
        ]


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


