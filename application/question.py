from quiz_utils import*


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