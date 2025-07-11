# homework 3

# Task 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruit=['peach', 'appricot', 'grapes', 'pineapple','orange']
print(fruit[2])

# Task 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

first_list=[1, 2, 3, 4, 5]
second_list=[6, 7, 8, 9]

concat_list=first_list+second_list
print(concat_list)

# Task 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

first_list=[1, 2, 3, 4, 5]
list_len=len(first_list)
if list_len % 2 ==0:
    mid_list=int(list_len/2)
else:
    mid_list=int(list_len/2+1)
print(f"First element is {first_list[0]}, middle element is {first_list[mid_list]}, last element is {first_list[-1]}")

#Task 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

my_list=['samsung', 'lg', 'sony', 'nokia']
my_tuple=tuple(my_list)
print(my_tuple)

# Task 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

my_list=['London', 'Berlin', 'Paris', 'Madrid', 'Rome']
check='Paris'

if check in my_list:
    print(check)
else:
    print(f"The text {check} is not in the list")

# Task 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

my_list=[2, 8, 3, 5 , 23, 90]

new_list=my_list.copy()

print(new_list)

# Task 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

my_list=['London', 'Berlin', 'Paris', 'Madrid', 'Rome']

my_list[0], my_list[-1]=my_list[-1], my_list[0]
print(my_list)

# Task 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

my_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i=slice(3, 7)
print(my_tuple[i])

# Task 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

color_list=['red', 'yellow', 'blue', 'grean', 'blue', 'white', 'blue']
print(color_list.count('blue'))

# Task 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals=('wolf', 'cat', 'elephant','lion')
print(animals.index('lion'))

# Task 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

vegatables=('onion', 'potato', 'carrot', 'melon')
fruits=('grapes', 'lemon', 'peach')

plants=vegatables+fruits
print(plants)

# Task 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

vegatables_list=(['onion'], ['potato'], ['carrot'], ['melon'])
fruits_tuple=('grapes', 'lemon', 'peach')
print(f"The lengths of the vegatables list is {len(vegatables_list)} and lengths of the fruits tuple is {len(fruits_tuple)}.")

# Task 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

my_tuple=('ball', 'rocket', 'rope', 'streching bar')
my_list=list(my_tuple)

print(my_list)

# Task 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

my_tuple=(21, 56, 85, 36, 88, 11)
min_tuple=min(my_tuple)
max_tuple=max(my_tuple)

print(f"Min value in tuple is {min_tuple} and max value is {max_tuple}.")

# Task 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

my_tuple=(21, 56, 85, 36, 88, 11)
rev_tuple=my_tuple[::-1]
print(rev_tuple)
