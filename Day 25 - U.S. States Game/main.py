
import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)  # csv reader creates a loopable object
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)
#
# final_data = []
# for line in data:
#     final_data.append(line.strip("\n"))
#
# print(final_data)
