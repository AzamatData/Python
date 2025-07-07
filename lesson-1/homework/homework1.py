
#task 1. Given a side of square. Find its perimeter and area.
side=input('Enter the side of square: ')
result=int(side)*4
print(result)


# task 2. Given diameter of circle. Find its length.
import math
d=int(input('Enter the diameter of the curcle : '))
curcle_length=math.pi*d
print(curcle_length)

#Task 3. Given two numbers a and b. Find their mean.
a=12
b=24
mean=(a+b)/2
print(f"The mean of number {a} and {b} is {mean}")

#Task 4. Given two numbers a and b. Find their sum, product and square of each number.

a=4
b=5
sum=a+b
product=a*b
a_square=a**2
b_square=b**2
print(f"The sum of number {a} and {b} is {sum}")
print(f"The product of number {a} and {b} is {product}")
print(f"The square of number {a} is {a_square}")
print(f"The square of number {b} is {b_square}")
