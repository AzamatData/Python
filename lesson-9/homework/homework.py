# Homework 9:
# Object-Oriented Programming (OOP) Exercises
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    
    def __init__(self, radius):
        self.radius=radius
        # pass
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return math.pi*2*self.radius
c1=Circle(5)
print(c1.area())
print(c1.perimeter())


# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if (today.month, today.day)<(self.date_of_birth.month, self.date_of_birth.day):
            age-=1
        return age
p1=Person("Tom", "Karakalpakstan", date(2020, 3, 12))
print(p1.calculate_age())

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        if self.b==0:
            return "Error: Can't be divided by 0"
        return self.a-self.b    
    def multiply(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b

problem1=Calculator(14, 5)
print(f"{problem1.a} + {problem1.b} = {problem1.addition()}")
print(f"{problem1.a} - {problem1.b} = {problem1.subtraction()}")
print(f"{problem1.a} * {problem1.b} = {problem1.multiply()}")
print(f"{problem1.a} / {problem1.b} = {problem1.division()}")
# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return math.pi*2*self.radius
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1+self.side2+self.side3
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2 *(self.height+self.width)

radius=5
circle = Circle(radius)
print(f"The area of the circle with radious {radius} is {circle.area()}")
print(f"The perimeter of the circle with radious {radius} is {circle.perimeter()}")

l = 5
w = 7
rectangle = Rectangle(l, w)
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

# Print the results for the Rectangle
print("\nRectangle: Length =", l, " Width =", w)
print(f"Rectangle Area for height {l} and width {w} is {rectangle_area}")
print(f"Rectangle Perimeter with height {l} and width {w} is {rectangle_perimeter}")

base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

# Print the results for the Triangle
print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.area()
triangle_perimeter = triangle.perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)

# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
# Define a class called Node to represent a node in a binary search tree (BST)
class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 

# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else: 
            return "Can't pop from an empty stack."
        
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty Stack."
stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


print("Stack size:", stack.size())
print("Top element:", stack.peek())

popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# Define a class called Node to represent a node in a linked list
class Node:
    # Initialize the Node object with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class called LinkedList to represent a singly linked list
class LinkedList:
    # Initialize the linked list with an empty head node
    def __init__(self):
        self.head = None

    # Display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Insert a new node with the given data at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node with the given data from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the initial linked list
print("Initial Linked List:")
linked_list.display()

# Insert a new node with data 5 into the linked list
linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

# Delete a node with data 2 from the linked list
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 


# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def add_item(self, item_name, qty):
        item=(item_name, qty)
        self.items.append(item)
    
    def remove_item(self, item_name):
        for item in self.items:
            if item_name[0]==item_name:
                self.items.remove(item)
                
    def calculate_total(self):
        total=0
        for item in self.items:
            total +=item[1]
        return total
    
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove_item("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty) 

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack_data:
    def __init__(self):
        self.ls=[]
    
    def push(self, item):
        return self.ls.append(item)

    def pop(self):
        if not self.ls_empty():
            return self.ls.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")
    
    def display(self):
        print(f"Stack items: {self.ls}")
        
    def ls_empty(self):
        return len(self.ls)==0

stack1 = Stack_data()
stack1.push(8)
stack1.push(9)
stack1.push(12)
stack1.push(18)
stack1.push(20)

stack1.display()

popped_item=stack1.pop()
print(f"Popped item is {popped_item}")

stack1.display()

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Nothing to remove"
    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        print(self.items)

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)

queue.display()

dequeued = queue.dequeue()
print(f"dequeued item: {dequeued}")

queue.display()


# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers={}
    # create account
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number is already exists.")
        else:
            self.customers[account_number]=initial_balance
            print("Account successfully created.")
    # deposit
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number]+=amount
            print("Deposit successfully. ")

        else:
            print("Account doesn't exists. ")
    def make_withdraw(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number]>=amount:
                self.customers[account_number]-=amount
                print("Withdrawal successfull. ")
            else: 
                print("Insufficient amount. ")
        else:
            print("Account doesn't exist. ")
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance=self.customers[account_number]
            print(f"Account balance: {balance}")

        else:
            print("Account doesn't exist. ")

bank = Bank()
bank.create_account(1)
bank.check_balance(1)
bank.make_deposit(1, 1000)
bank.make_withdraw(1,400)
bank.check_balance(1)

bank.create_account(2)
bank.check_balance(2)
bank.make_deposit(2, 56000)
bank.make_withdraw(2,500)
bank.check_balance(2)
