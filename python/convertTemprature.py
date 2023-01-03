# Write a program to asks the user to enter a temperature and a unit
# and then convert the temperature based on the entered unit

def c_to_f(c):
    return (c * 9/5)+ 32

def f_to_c(f):
    return (f - 32) * 5/9

#Ask the user to enter a temperature and a unit

temp = float (input ("Please enter a temperature:  "))
unit = input ("Please enter 'C' for Celsuis or 'F' for Fahrenheit:  ")

# Convert the temperature to the opposite unit
if unit =='C':
    result = c_to_f(temp)
    print(f"{temp}°C is equal to {result}°F\n")
elif unit == 'F':
    result = f_to_c(temp)
    print(f"{temp}°F is equal to {result}°C\n")
else:
    print("Invalid unit! Please enter either 'F' or 'C'")