from datetime import date

birth_year = int(input("Please enter your birth year (YYYY): "))
birth_month = int(input("Please enter your birth month (MM): "))
birth_day = int(input("Please enter your birth day (DD): "))

birth_date = date(birth_year, birth_month, birth_day)

day_of_week = birth_date.weekday()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("You were born on a", days[day_of_week])