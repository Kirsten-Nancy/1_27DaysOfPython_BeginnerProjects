# Getting data from csv file-normal file read
# with open('weather_data.csv') as file:
#     data = file.readlines()

# Using csv
# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     # Skip the header
#     next(data)
#     temperatures = []
#     for row in data:
#         temp = int(row[1])
#         temperatures.append(temp)
#     print(temperatures)

# Using pandas

import pandas as pd

# data = pd.read_csv('weather_data.csv')
# data_dict = data.to_dict()
#
# # Get data in columns
# temperature_series = data["temp"]
# temp_list = temperature_series.to_list()
# # print(temp_list)
# # print(temperature_series.mean())
# # print(temperature_series.max())
#
# # Get data in rows
# # print row with highest temp
# hottest_day = data[data['temp'] == data['temp'].max()]
# # print(hottest_day)
#
# sunny_days = data[data['condition'] == 'Sunny']
# # print(sunny_days)
#
# grades_dict = {
#     'students': ['Anthony', 'Wrigley', 'Miranda'],
#     'grades': [80, 85, 90]
# }
#
# student_grades = pd.DataFrame(grades_dict)
# print(student_grades)
# student_grades.to_csv('student_data.csv')
squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(type(squirrel_data))
fur_color_series = squirrel_data['Primary Fur Color']
cinnamon = squirrel_data[fur_color_series == 'Cinnamon']
black = squirrel_data[fur_color_series == 'Black']
gray = squirrel_data[fur_color_series == 'Gray']

squirrel_category_dict = {
    'Fur color': ['cinnamon', 'black', 'gray'],
    'Count': [len(cinnamon), len(black), len(gray)],
}

squirrel_category_data = pd.DataFrame(squirrel_category_dict)
squirrel_category_data.to_csv('squirrel_color_data.csv')


