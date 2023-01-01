# Write a program that asks the user for the number of sides of a polygon 
# and then returns the sum of the angles of that polygon:

def polygon_angles(sides):
    """Calculate the sum of the angles of a polygon with `sides` sides."""
    return (sides - 2) * 180
# Ask user to enter input
sides = input("Enter the number of sides of the polygon: ")

# Convert the value to an integer
sides = int(sides)

# Calculate and print the sum of the angles of the polygon
print(f"The sum of the angles of a {sides}-sided polygon is {polygon_angles(sides)} degrees.")








