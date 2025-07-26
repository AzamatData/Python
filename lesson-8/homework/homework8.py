# Homework8:
# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises
# 1.	Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
num=5
try:
    res=num/0
except ZeroDivisionError:
    print("This number can't be divided by 0")
# 2.	Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try: 
    num=int(input("Enter a number: "))
except ValueError:
    print("num is not integer")
# 3.	Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    file_handle=open("somthing.txt")
except: FileNotFoundError
print("The file you tried to open not found!")
# 4.	Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try: 
    num1=input("Enter a number: ") 
    num2=int(input("Enter a number: "))
    l=num1+num2
except TypeError:
    print("TypeError is occured")
# 5.	Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try: 
    with open(r"C:\DumpStack.log") as file:
        file.read()
except PermissionError:
    print("You don't have enough privilege to open the file")
# 6.	Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    ls=['sake', 'make', 'bake', 'wake']
    i=0
    while i<=len(ls)+5:
        print(ls[i])
        i+=1
except IndexError:
    print("Index of the list is run out")
# 7.	Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    something=int(input("Enter something: "))
except KeyboardInterrupt:
    print("You didn't enter anything")
# 8.	Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a=6
    b=0
    c=a/b
except ArithmeticError:
    print("there is an error in Arithmetics")

# 9.	Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt") as f:
        f.read()
except UnicodeDecodeError:
    print("The file can't be opened due to different encoding characters")

# 10.	Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    class New_class:
        def __init__(self, name, age):
            self.name=name
            self.age=age
    ep1 = New_class('Otambet', 45)
    print(ep1.gender)

except AttributeError:
    print("there is an Attribute error")

# ________________________________________
# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises
# 1.	Write a Python program to read an entire text file.
try:
    with open("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "r") as f:
        cont=f.read()
        print(cont)
except FileNotFoundError:
    print("file not exist")
# 2.	Write a Python program to read first n lines of a file.
n = int(input("Enter the first n number of lines to display: "))

with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "r") as f:
    print(f"\n--- First {n} lines from file ---")
    for i in range(n):
        cont = f.readline()
        if not cont:
            break
        print(cont.strip())  # Use .strip() to remove extra newline

# 3.	Write a Python program to append text to a file and display the text.
with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "a") as f:
          f.write(f"\nPython is interesting!")
          
with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "r") as f:
    content=f.read()
    print(content)
# 4.	Write a Python program to read last n lines of a file.
n = int(input("Enter the last n number of lines to display: "))

with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "r") as f:
    print(f"\n--- Last {n} lines from file ---")
    for i in f.readlines()[-n:]:
        print(i.strip()) 

# 5.	Write a Python program to read a file line by line and store it into a list.

def file_read(fname):
        with open(fname) as f:   
                ls = f.readlines()
                print(ls)
file_read(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt")
     

# 6.	Write a Python program to read a file line by line and store it into a variable.
def file_read(fname):
    with open(fname, "r") as f:
        my_var=f.readlines()
        print(type(my_var))
file_read(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt")
# 7.	Write a Python program to read a file line by line and store it into an array.
ls=[]
with open(r"D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "r") as f:
    for i in f:
        ls.append(i.strip())
print(ls)  
# 8.	Write a Python program to find the longest words.
def max_len_word(fname):
    with open(fname,'r') as f:
        words=f.read().split()
    max_len=len(max(words,key=len))
    for i in words:
        if len(i)==max_len:
            return i
print(max_len_word("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt"))
# 9.	Write a Python program to count the number of lines in a text file.
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt"))
# 10.	Write a Python program to count the frequency of words in a file.
def word_count(fname):
    word_freq = {}

    with open(fname, 'r') as f:
        for line in f:
            words = line.split() 
            for word in words:
                word = word.strip().lower()
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    return word_freq

print("Number of words in the file:", word_count("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt"))
# 11.	Write a Python program to get the file size of a plain file.
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt"))

# 12.	Write a Python program to write a list to a file.
cars = ['BMV', 'Opel', 'Cobalt', 'Cherry', 'Spark', 'Nexia']
with open('cars.txt', "w") as myfile:
        for c in cars:
                myfile.write("%s\n" % c)

content = open('cars.txt')
print(content.read())

# 13.	Write a Python program to copy the contents of a file to another file.
from shutil import copyfile
copyfile("D:\Learning\DataAnalytics\Python\Class1\Class8\something.txt", "abd.txt")
# 14.	Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open('abd.txt') as fh1, open('cars.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
# 15.	Write a Python program to read a random line from a file.
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('abd.txt'))
# 16.	Write a Python program to assess if a file is closed or not.
f = open('cars.txt','r')
print(f.closed)
f.close()
print(f.closed)

# 17.	Write a Python program to remove newline characters from a file.
def remove_newlines(fname):
    new=[]
    flist = open(fname).readlines()
    for i in flist:
        line=i.rstrip('\n')
        new.append(line)
    return new

print(remove_newlines("cars.txt"))

# 18.	Write a Python program that takes a text file as input and returns the number of words in a given text file.
# •	Note: Some words can be separated by a comma with no space.
def count_file_words(fname):
     with open(fname) as f:
          data=f.read()
          data.replace(",", " ")
          return len(data.split())
print(count_file_words('abd.txt'))

# 19.	Write a Python program to extract characters from various text files and put them into a list.

import glob
new_copy=[]
file_name=glob.glob("*.txt")
for i in file_name:
        with open(i) as f:
            new_copy.append(f.read())
print(new_copy)  

# 20.	Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string, os
if not os.path.exists("Letters"):
        os.makedirs("Letters")
for l in string.ascii_uppercase:
     with open(f"Letters/{l}.txt",'w') as f:
          f.writelines(l)
# 21.	Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

def with_letters_by_line(num):
    import string
    with open("all_letters.txt",'w') as f:
         letter = string.ascii_uppercase
         letters = [letter[i:i + num] + "\n" for i in range(0, len(letter), num)]
         f.writelines(letters)
with_letters_by_line(3)
        
