# Homework Projects:
# Homework 1. ToDo List Application
# 1.	Define Task Class:
# o	Create a Task class with attributes such as task title, description, due date, and status.
# 2.	Define ToDoList Class:
# o	Create a ToDoList class that manages a list of tasks.
# o	Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# 3.	Create Main Program:
# o	Develop a simple CLI to interact with the ToDoList.
# o	Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# 4.	Test the Application:
# o	Create instances of tasks and test the functionality of your ToDoList.

class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status




class ToDoList:
    def __init__(self):
        self.tasks=[]   
    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title==title:
                task.status="Complete"
    def list_all(self):
        for task in self.tasks:
            print(f"{task.title}---{task.status}")

    def list_incomplete(self):
        for task in self.tasks:
            if task.status !="Complete":
                print(f"{task.title}---{task.status}")

def main():
    todo=ToDoList()
    while True:
        print("\n======Options======\n1. Add Task\n2. Mark Task Complete\n3. Show All Tasks\n4. Show Incomplete Tasks\n5. Exit")
        choice = input("Choose an option: ")
        if choice=="1":
            title=input("Title: ")
            desc=input("Description: ")
            due=input("Due Date: ")
            task=Task(title, desc, due)
            todo.add_task(task)
            print("Task added successfully!")
        
        elif choice=="2":
            title=input("Enter the task to mark as complete: ")
            todo.mark_complete(title)
        
        elif choice=="3":
            todo.list_all()

        elif choice=="4":
            todo.list_incomplete()
        
        elif choice=="5":
            break

        else:
            print("Invalid choice.")
        
main()

# Homework 2. Simple Blog System
# 1.	Define Post Class:
# o	Create a Post class with attributes like title, content, and author.
# 2.	Define Blog Class:
# o	Create a Blog class that manages a list of posts.
# o	Include methods to add a post, list all posts, and display posts by a specific author.
# 3.	Create Main Program:
# o	Develop a CLI to interact with the Blog system.
# o	Include options to add posts, list all posts, and display posts by a specific author.
# 4.	Enhance Blog System:
# o	Add functionality to delete a post, edit a post, and display the latest posts.
# 5.	Test the Application:
# o	Create instances of posts and test the functionality of your Blog system.

class Post:
    def __init__(self, title, content, author):
        self.title=title
        self.content=content
        self.author=author

class Blog:
    def __init__(self):
        self.posts=[]
    def add_post(self, post):
        self.posts.append(post)
    
    def list_posts(self):
        for post in self.posts:
            print(f"{post.title}---{post.content}-------{post.author}")
    
    def by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                print(f"{post.title}---{post.content}-------{post.author}")
                found = True
        if not found:
            print(f"No posts found by author: {author}")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title == title:
                print(f"Editing post: {post.title}")
                new_title = input("New title (leave blank to keep unchanged): ")
                new_content = input("New content (leave blank to keep unchanged): ")
                new_author = input("New author (leave blank to keep unchanged): ")

                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                if new_author:
                    post.author = new_author

                print("Post updated.")
                return
        print(f"Post '{title}' not found.")

    def show_latest(self, count):
        latest = self.posts[-count:] if count <= len(self.posts) else self.posts
        for post in reversed(latest):  # Show most recent first
            print(f"{post.title}---{post.content}-------{post.author}")

def main():
    blog = Blog()
    while True:
        print("\n===== Select Option =====")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Filter by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest N Posts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the title: ")
            cont = input("Type the post: ")
            author = input("Author: ")
            post = Post(title, cont, author)
            blog.add_post(post)
            print("Post is published.")

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter the author: ")
            blog.by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                n = int(input("How many recent posts do you want to see? "))
                blog.show_latest(n)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")
main()


# Homework 3. Simple Banking System
# 1.	Define Account Class:
# o	Create an Account class with attributes like account number, account holder name, and balance.
# 2.	Define Bank Class:
# o	Create a Bank class that manages a list of accounts.
# o	Include methods to add an account, check balance, deposit money, and withdraw money.
# 3.	Create Main Program:
# o	Develop a CLI to interact with the Banking system.
# o	Include options to add accounts, check balance, deposit money, and withdraw money.
# 4.	Enhance Banking System:
# o	Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# 5.	Test the Application:
# o	Create instances of accounts and test the functionality of your Banking system.

import datetime

class Account:
    def __init__(self,holder_name):
        opened_date = datetime.datetime.today()
        self.holder_name = holder_name
        self.opened_date = opened_date
        self.id = 0
        self.balance = 0
        self.closed_date = None
    def deposit_money(self,deposit):
        self.balance += deposit
        return self.balance
    def withdraw_money(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            return True
        return False
    def close_account(self):
        self.closed_date = datetime.datetime.today()
    def __str__(self):
        return f"Account Number: {self.id} | Holder Name: {self.holder_name} | Balance: {self.balance}"
    

class Bank:
    account_list = []
    last_id = 0
    def __init__(self,name):
        self.name  = name
    def add_account(self):
        self.last_id += 1
        holder_name = input("Enter Your Name: ")
        account_obj = Account(holder_name)
        account_obj.id = self.last_id
        self.account_list.append(account_obj)
        print(f"Acccount Number {self.last_id} was added successfully")
    def search(self,id):
        for obj in self.account_list:
            if obj.id == id:
                return obj
        return False
    def deposit_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            deposit_amount = int(input("Enter your deposit amount! ex: 1000$ 💸 "))
            balance = a.deposit_money(deposit_amount)
            print(f"Depositing Process is completed successfully | Current Balance: {balance}")
        else:
            print(f"Account Number {id} is not found")
    def withdraw_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            withdraw_amount = int(input("Enter withdraw amount "))
            result = a.withdraw_money(withdraw_amount)
            if result:
                print(f"The withdraw process completed successfully! withdraw Amount: {withdraw_amount} | Current Balance: {a.balance}")
            else:
                print(f"Your account has not available amount! Amount: {withdraw_amount} | Current Balance: {a.balance}")
    def show_accounts_details(self):
        for i in self.account_list:
            print(i)
    def show_specific_account(self,id):
        a =  self.search(id)
        print(a)
    def close_account(self,id):
        a = self.search(id)
        a.close_account()
        print(f"Account Number {a.id} is closed")

milly_bank = Bank('milliy bank')
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")



while True:
    print_menu()
    command = input("Enter a number: ")
    if command == '1':
        milly_bank.add_account()
    elif command == '2':
        milly_bank.show_accounts_details()
    elif command == '3':
        account_number = int(input("Enter account Number: "))
        milly_bank.deposit_account(account_number)
    elif command == '4':
        account_number = int(input("Enter account Number: "))
        milly_bank.withdraw_account(account_number)
    elif command == '5':
        account_number = int(input("Enter account Number: "))
        milly_bank.show_specific_account(account_number)
    else:
        exit()
