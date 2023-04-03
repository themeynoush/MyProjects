# write a function that converts sq feet to sq meters
# 1 sq meter = 10.7639 sq feet
def sqfeetTosqmeter(sqfeet):
    sqmeter = sqfeet / 10.7639
    return sqmeter

# write a function that converts sq meters to sq feet
# 1 sq meter = 10.7639 sq feet  
def sqmeterTosqfeet(sqmeter):
    sqfeet = sqmeter * 10.76391
    return sqfeet

# ask the user to choose between sq feet and sq meters
print("Enter 1 for sq feet to sq meters")
print("Enter 2 for sq meters to sq feet")
choice = int(input("Enter your choice: "))

# if the user chooses 1
if choice == 1:
    # for the number of sq feet
    sqfeet = float(input("Enter the number of sq feet: "))
    # call the function
    sqmeter = sqfeetTosqmeter(sqfeet)
    # display the result
    print("The number of sq meters is", sqmeter)
# if the user chooses 2
elif choice == 2:
    # for the number of sq meters
    sqmeter = float(input("Enter the number of sq meters: "))
    # call the function
    sqfeet = sqmeterTosqfeet(sqmeter)
    # display the result
    print("The number of sq feet is", sqfeet)
else:
    print("Invalid choice")
    
# 
# for the number of sq feet
sqfeet = float(input("Enter the number of sq feet: "))
# call the function
sqmeter = sqfeetTosqmeter(sqfeet)
# display the result
print("The number of sq meters is", sqmeter)

# ask the