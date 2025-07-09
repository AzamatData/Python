# Homework Exercises
# Task 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name=input('Enter your name: ')
birth_year=int(input('Enter your Year of Birth: '))
print(f'Hello {name}, Your age is {2025-birth_year}.')

# Task 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])

# Task 3. Extract Car Names
# Extract car names from the following text:

txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[::-2])

# Task 4. Extract Residence Area
# Extract the residence area from the following text:

txt = "I'am John. I am from London"
city=txt.split("from")[-1].strip()
print(city)

# Task 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

user_input=input("Enter the text to be reversed: ")
reverse=user_input[::-1]
print(reverse)

# Task 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
user_input=input("Enter the text to count vowels: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(1 for ch in user_input 
        if ch in vowels)

print("Number of vowels:", c)

# Task 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers_string=input("Enter the list of numbers with white space: ")
delimiter = numbers_string.split()
to_list=max(list(map(int, delimiter)))
print(to_list)

# Task 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

user_input=input("Enter the text to check palindrome: ")
if user_input==user_input[::-1]:
    print("The text is palindrome")
else:
    print("The text is not palindrome")

# Task 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

user_input=input("Enter the email: ")
dom_part = user_input.split("@")[1]
print(dom_part)

# Task 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

# import modules
import string
import random


# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# check this input is it number? is it more than 8?
while True:

    try:

        characters_number = int(user_input)

        if characters_number < 8:

            print("Your number should be at least 8.")

            user_input = input("Please, Enter your number again: ")

        else:

            break

    except:

        print("Please, Enter numbers only.")

        user_input = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):

    result.append(s3[x])
    result.append(s4[x])


# shuffle result
random.shuffle(result)


# join result
password = "".join(result)
print("Strong Password: ", password)
