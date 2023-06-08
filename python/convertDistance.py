# Write a program that asks the user for a distance in km and converts it to mile and vice versa
# Author: Meynoush

# Define a function that convers km to mile
def convert_km_to_mile(km):
    return km * 0.621371 # 1 km = 0.621371 miles

def convert_mile_to_km(mile):
    return mile * 1.60934 # 1 mile = 1.60934 km

# Ask the user for the distance in km to convert it to miles
km = int(input("Enter a distance in km: "))

# Call the function and print the results
print(km, "=", convert_km_to_mile(km), "miles")

# ask the user for the distance in miles to convert it to km
mile = int(input("Enter the distance in mile: "))

# Call the function and print the results
print(mile, "=", convert_mile_to_km(mile), "kms")
