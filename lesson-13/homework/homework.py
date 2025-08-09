# Homework:
# 1.	Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import datetime, timedelta
from calendar import monthrange


birthday_input = input('Enter date and time (YYYY-MM-DD): ')
try:
    birthday = datetime.strptime(birthday_input, "%Y-%m-%d").date()
    current_date = datetime.now().date()

    years = current_date.year-birthday.year
    months = current_date.month-birthday.month
    days = current_date.day - birthday.day

    if days < 0:
        months -=1
        previous_month = current_date.month-1
        previous_year = current_date.year if current_date.month != 1 else current_date.year - 1
        days += monthrange(previous_year, previous_month)[1]

    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")

except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


# 2.	Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, date

birthday_input = input('Enter your birthday (YYYY-MM-DD): ')
try:
    birthday = datetime.strptime(birthday_input, "%Y-%m-%d").date()
    today = date.today()

    next_birthday = date(today.year, birthday.month, birthday.day)

    if next_birthday < today:
        try:
            next_birthday = date(today.year + 1, birthday.month, birthday.day)
        except ValueError:
            next_birthday = date(today.year + 1, 2, 28)

    days_remaining = (next_birthday - today).days
    print(f"Your next birthday is in {days_remaining} days.")

except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# 3.	Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

date_time_input = input('Enter current date and time (YYYY-MM-DD HH:MM): ')
duration_input = input('Enter the duration of the meeting in hours and minutes (HH:MM): ')

try:
    current_dt = datetime.strptime(date_time_input, "%Y-%m-%d %H:%M")

    hours, minutes = map(int, duration_input.split(":"))

    end_dt = current_dt + timedelta(hours=hours, minutes=minutes)

    print("The meeting will end:", end_dt.strftime("%Y-%m-%d %H:%M"))

except ValueError as e:
    print("Invalid input! Please follow the format: YYYY-MM-DD HH:MM for date and HH:MM for duration.")

# 4.	Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
from zoneinfo import ZoneInfo

date_time_input = input("Enter date and time (YYYY-MM-DD HH:MM): ")
source_tz_input = input("Enter your current timezone (e.g., Asia/Tashkent): ")
target_tz_input = input("Enter the target timezone (e.g., America/New_York): ")

try:
    naive_dt = datetime.strptime(date_time_input, "%Y-%m-%d %H:%M")

    source_dt = naive_dt.replace(tzinfo=ZoneInfo(source_tz_input))

    target_dt = source_dt.astimezone(ZoneInfo(target_tz_input))

    print(f"\nOriginal time in {source_tz_input}: {source_dt.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"Converted time in {target_tz_input}: {target_dt.strftime('%Y-%m-%d %H:%M %Z')}")

except ValueError:
    print("Invalid date/time format! Please use YYYY-MM-DD HH:MM.")
except ZoneInfo.KeyError:
    print("Invalid timezone name! Please use a valid IANA timezone string.")

# 5.	Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time


target_input = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")

try:
    target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            print("Countdown finished!")
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time left: {days}d {hours:02}h {minutes:02}m {seconds:02}s", end="\r")

        time.sleep(1)  

except ValueError:
    print("Invalid format! Please use YYYY-MM-DD HH:MM:SS")
# 6.	Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

email_input = input("Enter e-mail address: ")
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(email_pattern, email_input):
    print("Valid email address")
else:
    print("Invalid email address")
# 7.	Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re

phone_input = input("Enter your phone number: ")
digits = re.sub(r'\D', '', phone_input)  

if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
elif len(digits) == 11 and digits.startswith('1'):

    formatted = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
else:
    formatted = "Invalid or unsupported phone number format"

print(formatted)

# 8.	Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

password_input = input("Enter password: ")

if len(password_input)>=8 and re.findall('[A-Z]', password_input) and\
      re.findall('[a-z]', password_input) and re.findall('[0-9]', password_input):
    print("Password is valid")
else:
    print("Password is Invalid")

# 9.	Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re
given_txt="I want to learn Python. Python is a popular programming language.Python can be used on a server to create web applications."

find_word = input("Enter the word to find: ")

clean_text = re.sub(r'[^\w\s]',' ',given_txt)
clean_text = re.sub(r'\s+', ' ', clean_text).strip()

words = clean_text.split()
count = sum(1 for w in words if find_word.lower()==w.lower())
    
print(f"The word \"{find_word}\" is occured {count} times in given text.")

# 10.	Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re

text = input("Enter the text: ")


full_dates = re.findall(r'\b\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])\b', text)

print("Found dates:")
for date in full_dates:
    print(date)

