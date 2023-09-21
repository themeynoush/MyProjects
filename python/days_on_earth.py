import datetime

# Input date in the format YYYY-MM-DD
input_date_str = input("Enter your birthday (YYYY-MM-DD): ")

try:
    # Convert the input string to a datetime object
    input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d").date()

    # Print today's date
    today_date = datetime.date.today()
    print("Today is:", today_date)

    # Calculate the difference in days 
    # num_days = (today_date - input_date).days
    num_days = (today_date - input_date).days

    print("It's been", num_days, "days that you are on earth!")

except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD.")
