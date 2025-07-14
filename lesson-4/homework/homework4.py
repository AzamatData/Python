# Dictionary Exercises
# Task 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict={
    'book_name': 'Tom',
    'release_date': '01/08/1963',
    'sold_city': 'Taxtakupir',
    'author': 'Robert Jarabandu'
}

sorted_mylist=dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_mylist)

# task 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

# Sample Dictionary:

# {0: 10, 1: 20}

# Expected Result:

# {0: 10, 1: 20, 2: 30}
my_dict={
    0: 10,
    1: 20
}
my_dict.update([(2, 30)])
print(my_dict)

# Task 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionaries:

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result:

# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concated_dict={}
for i in (dic1, dic2, dic3):
    concated_dict.update(i)
print(concated_dict)

# Task 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num=int(input("Enter the number: "))
list_dict=dict()
for i in range(1, num+1):
    list_dict[i]=i*i
print(list_dict)

# Task 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the 
# values are the square of the keys.

# Expected Output:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

num=15
list_dict=dict()
for i in range(1, 15+1):
    # dict_square=[num, num*num]
    list_dict[i]=i*i
print(list_dict)

# Set Exercises
# Task 1. Create a Set
# Write a Python program to create a set.

my_set={'cats', 'dogs', 'hen', 'cow'}
print(my_set)

# Task 2. Iterate Over a Set
# Write a Python program to iterate over sets.

my_set={'cats', 'dogs', 'hen', 'cow'}
for i in my_set:
    print(i)

# Task 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

set_to_add={'Monday', 'Tuesday', 'Wednesday', 'Thursday'}
set_to_add.add('Friday')
print(set_to_add)

# Task 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

set_to_remove={'nexia', 'cobalt', 'malibu', 'bmw'}
set_to_remove.remove('bmw')
print(set_to_remove)

# Task 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

my_set={3, 5, 9, 8, 6}
my_set.discard(1)
print(my_set)
