from datetime import datetime

b_day = datetime(year = 1973, month = 9, day = 20)
today = datetime(year = 2023, month = 9, day = 20)
difference = today - b_day
print("It's been =", difference)