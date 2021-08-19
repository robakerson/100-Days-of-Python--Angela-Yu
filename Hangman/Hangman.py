

import random
import hangman_words
import hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessed_letters =[]
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letters:
      guessed_letters += guess
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
      #Check if user is wrong.
      if guess not in chosen_word:
          lives -= 1
          print(f"{guess} is not in the word!")
          if lives == 0:
              end_of_game = True
              print("You lose.")
    else:
      print(f"You've already guessed {guess}. Try something else!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])


# # step 3 we add a loop to allow multiple guesses
# display = []
# for _ in range(word_length):
#     display += "_"
# while "_" in display:
#   guess = input("Guess a letter: ").lower()
#   #Check guessed letter
#   for position in range(word_length):
#       letter = chosen_word[position]
#       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#       if letter == guess:
#           display[position] = letter
#   print(display)
# print("You win")

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
