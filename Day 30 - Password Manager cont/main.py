
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be higher than 3 meters.")

BMI = weight / height ** 2
print(bmi)



# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["wrong_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist!")
# else:
#     content = file.read()
#     print(content)
#
# file.close()

#  try/except/else/finally:
#  try: try this first
#  except: do this if there was an exception
#  else: do this if there were NO exceptions
#  finally: do this no matter what
