








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
