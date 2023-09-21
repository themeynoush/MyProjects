
import datetime

# Input date in the format YYYY-MM-DD
input_date_str = input("Enter a date (YYYY-MM-DD): ")
num_days = int(input("Enter the number of days: "))

try:
    # Convert the input string to a datetime object
    input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d")

    # Add 20,000 days to the input date
    new_date = input_date + datetime.timedelta(days=num_days)

    # Format and print the new date
    new_date_str = new_date.strftime("%Y-%m-%d")
    print(f"The date after, {num_days} days will be: {new_date_str}")

except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD.")
