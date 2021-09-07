
import pandas

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
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # create dataframe from dictionary!
data.to_csv("new_data.csv")  # convert data into .csv file!



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
