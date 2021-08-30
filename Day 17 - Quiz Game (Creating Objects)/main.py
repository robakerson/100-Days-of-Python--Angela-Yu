
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:  # each entry in question_data is a dictionary
    text = question['question']
    answer = question['correct_answer']
    cur_question = Question(text, answer)  # create question object from current text:answer dictionary KVP
    question_bank.append(cur_question)  # append current question to question_bank list

quiz = QuizBrain(question_bank)  # QuizBrain object contains the methods we will use to run our quiz!
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# print(question_bank[0].text)

# # new class
# class User:
#     pass
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0  # default value
#         self.following = 0
#
#     def follow(self, user):
#         user.followers +=1
#         self.following +=1
#
# # # defining attributes on the object instead of the class
# # user_1.id = "001"
# # user_1.username = "Bob"
#
# user_1 = User("001", "Bob")  # Have to provide values or class won't create
# user_2 = User("002", "Jack")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
