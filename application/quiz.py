from question import*


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