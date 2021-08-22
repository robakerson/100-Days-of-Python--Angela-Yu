


# travel_log= {
#   #dictionary in a dictionary
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon",]},
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# print(travel_log["France"]["cities_visited"][0])

# #create list with 2 dictionary elements, each dictionary has 3 entries, one of which is a list...
# travel_log = [
#   {"country": "France",
#   "cities_visited": ["Paris", "Lille", "Dijon"],
#   "total_visits": 12}
#   {"country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5}
# ]
# print(travel_log[0]["country"])



# # declare student_scores
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# #init student_grades as empty dictionary
# student_grades = {}
# # loops once for each entry in student_scores dictionary. key = "Harry", "Ron", etc
# for key in student_scores:
#     #case/switch for student scores adds KVP for "Student":"Outstanding"/"Exceeds Expectations"/etc to student_grades dictionary
#   if student_scores[key] > 90:
#     student_grades[key] = "Outstanding"
#   elif student_scores[key] > 80 and student_scores[key] <91:
#     student_grades[key] = "Exceeds Expectations"
#   elif student_scores[key] > 70 and student_scores[key] <81:
#     student_grades[key] = "Acceptable"
#   elif student_scores[key] <= 70:
#     student_grades[key] = "Fail"
#
# print(student_grades)


# ## dictionary 101 stuff below ##
# #declare dictionary
# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Loop": "The action of doing something over and over again.",
# }
# #retrieving items from dictionary
# print(programming_dictionary["Bug"])
# #Adding new items to dictionary
# programming_dictionary["Loop"]= "The action of doing something over and over again."
# #declare empty dictionary
# empty_dictionary = {}
# #wipe existing dictionary
# programming_dictionary = {}
# #edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# #loop through a dictionary
# for key in programming_dictionary:
#   #print keys only
#   print(key)
#   #print the values
#   print(programming_dictionary[key])
