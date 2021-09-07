
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"])

primary_fur_colors = ["Gray", "Cinnamon", "Black"]
color_count = []
for color in primary_fur_colors:
    color_count.append(len(data[data["Primary Fur Color"] == color]))  # create list of count of each fur color

color_dict = {
    "Fur Color": primary_fur_colors,
    "Color": color_count
}

final_data = pandas.DataFrame(color_dict)
print(final_data)
final_data.to_csv("Squirrel_count.csv")  # create csv file from our data!

# color_table = []
# for elem in range(len(primary_fur_colors)):
#     color_table.append([primary_fur_colors[elem], color_count[elem]])  # create list of lists of [color, count]
#
# final_table = pandas.DataFrame(color_table)
# print(final_table)

# gray_col = data[data["Primary Fur Color"] == "Gray"]
# cinnamon_col = data[data["Primary Fur Color"] == "Cinnamon"]
# black_col = data[data["Primary Fur Color"] == "Black"]

# print(len(gray_col))
# print(len(cinnamon_col))
# print(len(black_col))


# print(data[data["Primary Fur Color"] == "Gray"])

# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])  # print temperature column
# print(data.temp)  # print temperature column
# temp_list = data["temp"].to_list() # convert column to a list
# # print(temp_list)
# print(sum(temp_list) / len(temp_list))  # print average temperature
# print(data["temp"].mean())  # print average temperature
# print(data[data.day == "Monday"])  # print the row with "Monday" day
# print(data[data.temp == data.temp.max()])  # print the row which contains the highest temperature
# monday = data[data.day == "Monday"]
# print(int(monday.temp))

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)  # create dataframe from dictionary!
# data.to_csv("new_data.csv")  # convert data into .csv file!



# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)  # csv reader creates a loopable object
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)
#
# final_data = []
# for line in data:
#     final_data.append(line.strip("\n"))
#
# print(final_data)
