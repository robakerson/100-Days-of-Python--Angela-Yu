class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        question_list_length = len(self.question_list)
        return self.question_number < question_list_length

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        self.check_answer(answer, question_answer)
        print(f"Your current score is: {self.score}/{self.question_number} \n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")

