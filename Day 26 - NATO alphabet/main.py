
import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# student_data_frame = pandas.DataFrame(student_dict)
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

with open("nato_phonetic_alphabet.csv") as file:
    NATO_phonetic = pandas.read_csv(file)

NATO_dict = {row.letter: row.code for (index, row) in NATO_phonetic.iterrows()}
# print(NATO_dict)
good_word = False

while not good_word:
    user_word = input("Please input a word to translate into the NATO phonetic alphabet!: ")
    try:
        code_words = [NATO_dict[letter.upper()] for letter in user_word]
        good_word = True
    except KeyError:
        print("Please only enter letters that exist ")


# code_words = [NATO_dict[letter.upper()] for letter in user_word]
print(code_words)
