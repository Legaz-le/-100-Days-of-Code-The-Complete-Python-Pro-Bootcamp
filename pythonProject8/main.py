# with open ("weather_data.csv.csv") as data:
#     weather = data.readlines()
#     print(weather)
#
#
# import csv
#
#
# with open ("weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#

import pandas

# data = pandas.read_csv("new_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].max())
# print(data["temp"].mean())
# #Get data in Column
# print(data["condition"])
# print(data.condition)
#Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# this was test:
# squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240927.csv")
#
# colum = (squirrel["Primary Fur Color"])
#
# Gray = len(squirrel[colum == "Gray"])
# Cinnamon = len(squirrel[colum == "Cinnamon"])
# Black = len(squirrel[colum == "Black"])
#
# print(Gray)
# squirrel_data = {
#     "Primary Fur Color": ["Gray","Cinnamon", "Black"],
#     "sum": [Gray,Cinnamon,Black]
# }
# data = pandas.DataFrame(squirrel_data)
# data.to_csv("squirrel_count")