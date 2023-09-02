try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator
    print("The division result is: "+ str(result))

    my_list = [11,12,13]
    i = int(input("Enter index: "))
    print(my_list[i]) #if i >= 3, returns an index error

except ZeroDivisionError:
    print("The denominator cannot be Zero! Please try again")

except IndexError:
    print("The index number is out of range.")


