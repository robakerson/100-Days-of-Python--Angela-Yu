

# # select random word from list
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# # create "display" list that will store correct guesses and remaining empty spots
# display = []
# # add a _ for each letter in randomly selected word to display
# for letter in chosen_word:
#   display += "_"
#
#  # prompt user for an input. Check each letter of chosen_word for that guess.
#  # if user guess matches letter from chosen_word, we replace that element from display list with the letter
# guess = input("Guess a letter: ").lower()
# for letter in range(len(chosen_word)):
#     if chosen_word[letter] == guess:
#         display[letter]=guess
# print(display)

#######################

# #challenge 1 take input from user, select random word, check if user's input matches letters in that word
# import random
# word_list = ["aardvark", "baboon", "camel"]
# # select random word from word_list
# # chosen_word = word_list[random.randint(0,len(word_list)-1)]
# chosen_word = random.choice(word_list)
# #take input from user and assign it to guess
# guess = input("Guess a letter of the word:")
# # check each letter in randomly chosen word against user guess and print whether it matches
# for letter in chosen_word:
#   if letter == guess:
#     print("Correct")
#   else:
#     print("Wrong")
