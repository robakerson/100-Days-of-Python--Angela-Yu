
#Full Calculator
#Add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  num1 = float(input("What's the first number?: "))
  another_operation = True
  #if user wants to keep going, we ask for another operation and number and operate on previous result
  while another_operation:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above:" )
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer= calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:")
    if continue_prompt == 'y':
      num1 = answer
    else:
      another_operation = False
      print(f"Your final result is {answer}")
      #The calculator calls itself. WE NEVER STOP
      calculator()

calculator()







# #First Calculator - one calculation
# #Add
# def add(n1, n2):
#   return n1 + n2
# #subtract
# def subtract(n1, n2):
#   return n1 - n2
# #multiply
# def multiply(n1, n2):
#   return n1 * n2
# #divide
# def divide(n1, n2):
#   return n1 / n2
#  #dictionary holds the operations we will use. user input is the key, value determines the function to call from above
# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }
# #user inputs number, operation, number2
# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#   print(symbol)
# operation_symbol = input("Pick an operation from the line above:" )
# num2 = int(input("What's the second number?: "))
# # call one of the 4 operation functions based on which user input is given and call that function with number inputs
# answer= operations[operation_symbol](num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")

# #leap year function
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
#
# #days_in_month function takes year,month and returns number of days
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and int(month) == 2:
#     return 29
#   else:
#     return month_days[month - 1]
#
# #call above functions with user input
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# # function with multiple inputs, one output
# def format_name(f_name, l_name):
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"
# # print the output of the format_name function
# print(format_name("anGelA", "yU"))
