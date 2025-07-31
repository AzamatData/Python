# Homework:
# 1.	Create your own virtual environment and install some python packages.
# (in terminal)
# cd D:\Learning\DataAnalytics\Python\Class1\Class11\
# mkdir MyVenv
# cd D:\Learning\DataAnalytics\Python\Class1\Class11\MyVenv 
# python -m venv myenv
# Set-ExecutionPolicy Unrestricted -Scope Process
# .\myenv\Scripts\Activate 

# pip install cowsay
# installed, in my *.py file I write this code
import cowsay

cowsay.cow("Good Mooooorning!")

# 2.	Create custom modules.
# o	Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)

# math_operations.py module as following
# math_operations.py
# =====================
# import math

# def add(a, b):
#     return a+b

# def subtract(a, b):
#     return a-b

# def multiply (a, b):
#     return a*b

# def divide(a, b):
#     return a/b
# =================
import math_operations as m
print(m.add(2, 8))
print(m.subtract(2, 8))
print(m.multiply(2, 8))
print(m.divide(2, 8))

# o	Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
import string_utils as s
print(s.reverse_string("Ayjamal"))
print(s.count_vowels("Ayjamal"))
# 3.	Create custom packages.
# o	Create geometry package.

# 	 geometry\
# from terminal:
# mkdir geometry
# cd geometry
# 	     __init__.py
# New-Item -Path "__init__.py" -ItemType File
#        circle.py
# New-Item -Path "circle.py" -ItemType File
# Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
# circle.py file is as following:
# circle.py
# =========================
# import math
# def calculate_area(radius):
#     area=math.pi*(radius**2)
#     return area

# def calculate_circumference(radius):
#     circumference=2 * math.pi * radius
#     return circumference
# ==========================


from geometry import circle
print(circle.calculate_area(5))

print(circle.calculate_circumference(6))
 
# o	Create file_operations package.
#  file_operations\
#      __init__.py
#      file_reader.py
#      file_writer.py
 
# Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).
# in terminal
# mkdir file_operations
# cd file_operations
# 	     __init__.py
# New-Item -Path "__init__.py" -ItemType File
# New-Item -Path "file_reader.py" -ItemType File
# New-Item -Path "file_writer.py" -ItemType File
from file_operations import file_reader
file_reader.read_file("test_file.txt")

from file_operations import file_writer
file_writer.write_file("test_file.txt", "I hope this works well...")

