# Convert the user's hight from the European system to the American system 

def convert_hight(height_cm):
   # height_inches = height_cm / 2.54 #cm to inches 
    height_feet = int(height_cm // 30.48) # inches to feet 
    remaining_cm = float(height_cm % 30.48)
    height_inches = remaining_cm / 2.54 #cm to inch
    print("Your height is {} feet and {:.3f} inches.".format(height_feet, height_inches))

user_height= float(input("Enter your height in cm:"))
convert_hight(user_height)
