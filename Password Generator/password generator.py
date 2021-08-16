
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
