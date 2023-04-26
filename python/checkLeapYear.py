# define a function to check if a year is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# ask the user to enter a year
year = int(input("Enter a year: "))

# Print the result if the year is a leap year
if isLeapYear(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
