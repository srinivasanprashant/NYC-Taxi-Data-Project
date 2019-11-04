import csv
import numpy as np

import time


# import nyc_taxi.csv as a list of lists using open and conversion to floats
def open_file_costly():
    with open("nyc_taxis.csv", "r") as f:
        taxi_list = list(csv.reader(f))
    # remove the header row after saving it for future reference
    # taxi_header = taxi_list[0]
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
    np_taxi = np.array(converted_taxi_list)
    return np_taxi


#  Demonstrating more efficient way of importing numerical data from a csv file
def open_file_numpy():
    np_taxi = np.genfromtxt("nyc_taxis.csv", delimiter=",", skip_header=1)
    return np_taxi


# t0 = time.perf_counter()
# taxi = open_file_costly()
# t1 = time.perf_counter() - t0
# print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
# print(taxi)
# print(taxi.shape)
print("Using Numpy")
t0 = time.perf_counter()
taxi = open_file_numpy()
t1 = time.perf_counter() - t0
print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)
print(taxi)
print(taxi.shape)


# fare_amount = taxi[:, 9]
# fees_amount = taxi[:, 10]
# fare_and_fees = fare_amount + fees_amount
# trip_distance_miles = taxi[:, 7]
# trip_length_seconds = taxi[:, 8]
#
# trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
# trip_mph = trip_distance_miles / trip_length_hours
# mph_min = trip_mph.min()
# mph_max = trip_mph.max()
# mph_mean = trip_mph.mean()
# mph_median = np.median(trip_mph)
# print(mph_min, mph_max, mph_mean, mph_median, trip_mph.shape)
# # let's clean up some of he data to remove to very high max speeds. For now, let's keep data where avg. speed < 100
# bool_trip_mph = trip_mph < 100
# trip_mph_mask = trip_mph[bool_trip_mph]
# # Now let's remove all trips where avg. speed was 0
# bool_trip_mph = trip_mph != 0
# trip_mph_mask = trip_mph[bool_trip_mph]
# mph_min = trip_mph_mask.min()
# mph_max = trip_mph_mask.max()
# mph_mean = trip_mph_mask.mean()
# mph_median = np.median(trip_mph_mask)
# print(mph_min, mph_max, mph_mean, mph_median, trip_mph_mask.shape)
#
# # we'll compare against the first 5 rows only
# taxi_first_five = taxi[:5]
# # select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
# fare_components = taxi_first_five[:,9:13]
# fare_sums = fare_components.sum(axis=1)
# fare_totals = taxi_first_five[:, 13]
# print(fare_sums - fare_totals)

# tip_amount = taxi[:, 12]
# tip_bool = tip_amount > 50
# top_tips = taxi[tip_bool, 5:14]
# print(top_tips[:5, 4:])

# We want to figure out which airport is the most popular destination in our data set
# We will use boolean indexing to create three filtered arrays and then look at how many rows are in each array

# Calculate how many trips had JFK Airport as their destination
# For JFK Airport, drop-off_location_code (column index 6) is 2
jfk_bool = taxi[:,6] == 2
jfk = taxi[jfk_bool, 6]
jfk_count=jfk.shape[0]
# Calculate how many trips from taxi had Laguardia Airport as their destination
# For LaGuardia Airport, drop-off_location_code (column index 6) is 3
laguardia_bool = taxi[:,6] == 3
laguardia = taxi[laguardia_bool, 6]
laguardia_count=laguardia.shape[0]
# Calculate how many trips from taxi had Newark Airport as their destination
# For Newark Airport, drop-off_location_code (column index 6) is 5
newark_bool = taxi[:, 6] == 5
newark = taxi[newark_bool, 6]
newark_count=newark.shape[0]
# Display the drop-off data that was computed from the data-set
print("JFK Drop-offs: ", jfk_count)
print("LaGuardia Drop-offs: ", laguardia_count)
print("Newark Drop-offs: ", newark_count)

# Remove potentially bad data from our data set by checking for average speed < 100
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph<100,:]
# Use array methods to calculate the mean for specific columns of the remaining data
mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()

print("Mean Distance: {:.2f} miles".format(mean_distance))
print("Mean Length: {:.2f} minutes".format(mean_length/60))
print("Mean Total Amount: ${:.2f}".format(mean_total_amount))
