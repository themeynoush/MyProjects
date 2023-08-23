# Write a program that asks the user to inter an int and reverse the int

# Ask the user to enter a positive integer number
num = int(input("Please enter a positive integer number:"))
print("The original number is:", num)

# Reverse the given number
# reverse = 0
# while num!=0:
#     reverse = reverse*10 + num%10
#     num = (num//10)

# Print the results
#print("The reversed number is:", reverse)


# The second way of doing it is 
# rev = int(str(num)[::-1])
# print("The reversed number using slicing: ", rev)


# Reverse the number Using Recursion
def reverse(num):
    if num < 10:
        return num
    else:
        return (num%10) * 10**(len(str(num))-1) + reverse(num // 10)
    # if num < 10:
    #     return num
    # else:
    #     return (num % 10) * 10**(len(str(num))-1) + reverse(num // 10)

reversed_num = reverse(num)
print("The reversed number using recursion:", reversed_num)