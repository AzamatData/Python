# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, 
# shift the underscore placement to the next character. No underscore should be added at the end.

# Examples
# Input: hello Output: hel_lo

# Input: assalom Output: ass_alom

# Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef
# my_txt = 'assalom'
my_txt='abcabcabcdeabcdefabcdefg'
used_chars = ['a', 'e', 'i', 'o', 'u']
i=2

while i<len(my_txt)-1:
    if my_txt[i] not in used_chars:
        my_txt=my_txt[:i+1]+'_'+ my_txt[i+1:]
        used_chars.append(my_txt[i])
        i+=4
    else:
        i+=1
print(my_txt)

# Task 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

# Example Input
# 5
# Example Output
# 0
# 1
# 4
# 9
# 16

# Input Format
# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20
# Output Format
# Print n lines, one corresponding to each i^2 where 0 <= i < n.

n=int(input("Enter the number: "))
if n>=1 and n<=20:
    for i in range(n):
        print(i*i)

# Task 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

n=(int)
n=1
while n<=10:
    print(n)
    n+=1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


i=1
while i<=5:
    n=1
    while n<=i:
        print(n, end=" ") 
        n+=1
    print()
    i+=1


# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:

# Enter number 10
# Sum is: 55
num=(int(input("Enter number ")))
i=1
my_sum=0
while i<=num:
    my_sum=my_sum+i
    i+=1
print(f"Sum is {my_sum}")

# Exercise 4: Print multiplication table of a given number
# Example:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num=(int(input("Enter the number: ")))
i=1
multi=0
while i<=10:
    multi=num*i
    print(multi)
    i+=1

# Exercise 5: Display numbers from a list using a loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:

# 75
# 150
# 145

index_num=1
i=0
numbers = [12, 75, 150, 180, 145, 525, 50]
while i*i<len(numbers):
    index_num=i*i
    print(numbers[index_num])
    i+=1

# Exercise 6: Count the total number of digits in a number
# Example:

# 75869
# Output: 5

number=75869
c=0
while number>0:
    number//=10
    c+=1
print(c)

# Exercise 7: Print reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

r=5
while r>=1:
    i=r
    while i>=1:
        print(i,end=" ")
        i-=1
    print()
    r-=1

# Exercise 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected Output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]
i=len(list1)-1
while i>=0:
    print(list1[i])
    i-=1

# Exercise 9: Display numbers from -10 to -1 using a for loop
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10, 0):
    print(i)
    i+=1

# Exercise 10: Display message “Done” after successful loop execution
# Example:

# 0
# 1
# 2
# 3
# 4
# Done!
n=int(input("Enter the number: "))
for i in range(n+1):
    print(i)
print("Done!")

# Exercise 11: Print all prime numbers within a range
# Example:

# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47


n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))

for i in range(n1, n2 + 1):
    if i <= 1:
        continue  # skip non-primes <= 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else: print(i)

# Exercise 12: Display Fibonacci series up to 10 terms
# Example:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

n = 10
a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120

n=1
s=1
while n<=5:
    s=n*s
    n+=1
print(f"# 5! = {s}")

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]

# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

# new_set=set(list1)^set(list2)
# print(new_set)
new_list=[]

for i in list1:
    if i not in list2:
        new_list.append(i)

for i in list2:
    if i not in list1:
        new_list.append(i)

print(new_list)
