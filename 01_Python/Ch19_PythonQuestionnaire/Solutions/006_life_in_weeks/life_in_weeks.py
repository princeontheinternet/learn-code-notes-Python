user_age = input("Enter your age: ")

age_left_in_years = 90 - int(user_age)

days_left = 365 * age_left_in_years
weeks_left = 52 * age_left_in_years
months_left = 12 * age_left_in_years

print(f"You have {days_left} days, {weeks_left} week, and {months_left} months.")