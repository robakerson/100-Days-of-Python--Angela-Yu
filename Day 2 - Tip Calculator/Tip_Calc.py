#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("Welcome to the tip calculator.")
bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give?")
people = input("How many people to split the bill?")

#final bill = bill + tip, where tip = bill * tip%
#all inputs converted to floats as they default as strings
final_bill = float(bill) + (float(bill) * float(tip) / 100)

# cost per person is total cost / number of people. Round to 2 decimals so the cost makes sense

cost_per_person = round(final_bill / int(people), 2)
print(f"Each person should pay: ${cost_per_person}")
