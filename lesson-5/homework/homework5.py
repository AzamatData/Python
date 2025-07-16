# Homework:
# Task 1

# def is_leap(year): """ Determines whether a given year is a leap year.

# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.

# Parameters:
# year (int): The year to be checked.

# Returns:
# bool: True if the year is a leap year, False otherwise.
# """
# if not isinstance(year, int):
#     raise ValueError("Year must be an integer.")

# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if (year % 4==0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False
        
print(is_leap(2024))

# Task 2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
n=(int(input("Enter the number: ")))

if n % 2 ==0 and n in range(2, 5):
    print("Not Wierd")

elif n % 2 ==0 and n in range(6, 20):
    print("Wierd")

elif n % 2 !=0:
    print("Wierd")

elif n % 2 ==0 and n>20:
    print("Not Wierd")

# Task 3.
# Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.

a=int(input("Enter the number for a: "))
b=int(input("Enter the number for b: "))

if a%2==0:
    print(list(range(a, b, 2)))
elif a%2 !=0:
    print(list(range(a+1, b, 2)))
# Solution 2 without if-else statement.

a=int(input("Enter the number for a: "))
b=int(input("Enter the number for b: "))

a=round(a/2)*2
print(list(range(a, b, 2)))
