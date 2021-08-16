
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# #print random number between 0-51
# print(random.randint(0,len(letters)-1))

# # solution with sequential letters, then symbols, then numbers
# for letter in range(0, nr_letters):
#   password += letters[random.randint(0,len(letters)-1)]
# for letter in range(0, nr_symbols):
#   password += symbols[random.randint(0,len(symbols)-1)]
# for letter in range(0, nr_numbers):
#   password += numbers[random.randint(0,len(numbers)-1)]
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

nr_chars = nr_letters + nr_symbols + nr_numbers
for number in range(0, nr_chars):
  #Each element of answer_list is the list of letters, symbols, or numbers. We randomly select from those elements to determine what to type next.
  answer_list = []
  for num_numbers in range(0,nr_numbers):
    answer_list.append(numbers)
  for num_letters in range(0,nr_letters):
    answer_list.append(letters)
  for num_symbols in range(0,nr_symbols):
    answer_list.append(symbols)
  #char_type_sel determines whether we are mining for numbers, symbols, or letters
  char_type_sel = random.randint(0,len(answer_list)-1)
  #char_sel determines which element of the array we are mining to put into the password
  char_sel = random.randint(0,len(answer_list[char_type_sel])-1)
  #decrement the type of character we used. Ensures we use correct number of each type of character
  if answer_list[char_type_sel] == letters:
    password += letters[char_sel]
    nr_letters -= 1
  elif answer_list[char_type_sel] == symbols:
    password += symbols[char_sel]
    nr_symbols -= 1
  else:
    password += numbers[char_sel]
    nr_numbers -= 1

print(password)




# practice programs for day 5:

# fruits = ["apple", "peach", "pear"]
#
# # will print each element of the fruits list
# for fruit in fruits:
#   print(fruit)


# # program to generate average value from a list of heights,
# # rounded to the nearest whole number without using sum() or len()
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# # variable to add all heights together
# sum_height = 0
# # variable to count number of height elements
# num_heights = 0
#
# #increment sum_height by current height value and increment num_heights by 1
# for height in student_heights:
#   sum_height += height
#   num_heights += 1
#
# #average is sum of all heights divided by number of heights
# print(round(sum_height / num_heights))

# # program to generate highest number in a list without using max()
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# #cur_max will track the highest encountered score thus far.
# # at the end, it will be the highest score in the list
# cur_max = 0
#
# #for loop grabs each score, then we check that score against the highest score found so far
# #if the current score is higher than the highest seen, that becomes the highest
# for score in student_scores:
#   if score > cur_max:
#     cur_max = score
#
# print(f"The highest score in the class is: {cur_max}")

# #print sum of all even numbers between 1-100
# sum_of_evens = 0
# for number in range(1, 101):
#   if number%2 ==0:
#     sum_of_evens += number
# print(sum_of_evens)

# # FizzBuzz but I don't do it the way she wants me to
# for number in range(1, 101):
#   print_val = number
#   if number%3 == 0:
#     if number%5 ==0:
#       print_val= "FizzBuzz"
#     else:
#       print_val= "Fizz"
#   elif number%5==0:
#     print_val="Buzz"
#   print(print_val)
