# with open("day-25-start\weather_data.csv", "r+") as data_file:
#     data =(data_file.readlines())
#     print(data)

# import csv

# with open("day-25-start\weather_data.csv", "r+") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
#     print(temperature)

import pandas

data = pandas.read_csv("day-25-start\weather_data.csv")
# print(data)
# print(data["temp"])
temp_list = data["temp"].to_list()
avg_temp = sum(temp_list)/len(temp_list)
print(f" The average Temperature is {avg_temp}")
print(f"The maximum value is {max(temp_list)}")
print(f"The day with the highest temperature is {data[data.temp == max(temp_list)]}")
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp  *9/5 + 32
print(monday_temp_f)
