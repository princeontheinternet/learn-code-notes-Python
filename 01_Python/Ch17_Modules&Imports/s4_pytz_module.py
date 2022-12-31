import pytz
import datetime


# Finding a string using substring
# for x in pytz.all_timezones:
#     if "India" in x:
#         print(x)


def get_country_code(country_name):
    for country_code in sorted(pytz.country_names):
        if pytz.country_names[country_code] == country_name:
            return country_code


def get_country_timezone(country_code):
    zones = []
    for i in pytz.country_timezones[country_code]:
        zones.append(i)
    return zones


# Country and Country Code
user_country_name = input("Enter the country name: ")
user_country_code = get_country_code(user_country_name)
print(f"Country =  {user_country_name} \nCode = {user_country_code}")

# Getting all the timezones
time_zones = get_country_timezone(user_country_code)
print(f"The timezones available for {user_country_code}: {time_zones}")

# Displaying local time
zone = input("Enter time zone: ")
local_time = datetime.datetime.now(tz=pytz.timezone(zone))
current = datetime.datetime.now()
print(f"Local Time: {local_time}")
print(f"Current Time = {current}")

