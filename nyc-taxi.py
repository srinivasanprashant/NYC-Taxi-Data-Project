import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
with open("nyc_taxis.csv", "r") as f:
    taxi_list = list(csv.reader(f))
# remove the header row after saving it for future reference
taxi_header = taxi_list[0]
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for data in row:
        try:
            converted_row.append(float(data))
        except ValueError:
            converted_row.append(float(0))
    converted_taxi_list.append(converted_row)

taxi = np.array(converted_taxi_list)
print(type(taxi))
