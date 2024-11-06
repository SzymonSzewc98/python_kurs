from instructor import*

"""
Debug file
"""

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


debug_test_question()
debug_instructor()



