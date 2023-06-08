# Write a program that asks the user for a distance in km and converts it to mile and vice versa
# Author: Meynoush

# Define a function that convers km to mile
def covnert_km_to_mile(km):
    return km * 0.621371 # 1 km = 0.621371 miles

def convert_mile_to_km(mile):
    return mile * 1.60934 # 1 mile = 1.60934 km

# ask the user for the distance in km to convert it to miles
km = int(input("Enter a distance in km: "))


# ask the user for the distance in miles to convert it to km
mile = int(input("Enter the distance in mile:"))



# ask the user for a weight in pounds
pounds = float(input("Enter a weight in pounds: "))
# call the function and print the result
print("That is", convert_pounds_to_kg(pounds), "kilograms.")
print("That is", convert_kg_to_stone(convert_pounds_to_kg(pounds)), "stones.")

