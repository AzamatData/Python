# Homework 14
# 1.	Task: JSON Parsing
# 	write a Python script that reads the students.jon JSON file and prints details of each student.
import json

with open("D:/Learning/DataAnalytics/Python/Class1/students.json") as f:
    my_dict = json.load(f)

for dict in my_dict['students']:
    print(f"The id of the student is {dict['id']}, name is {dict['name']}, age is {dict['age']}, grade is {dict['grade']}\
, the subjects are {dict['subjects']}, the address is {dict['address']}." )
    
# 2.	Task: Weather API
# i.	Use this url : https://openweathermap.org/
# ii.	Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests
my_url = 'https://api.openweathermap.org/data/2.5/weather'
my_api = '445bef235633be912621d8850a68cb58'
city = 'Tashkent'

response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+my_api+'&units=metric')

if response.status_code == requests.codes.ok:

    my_data = response.json()
    print(f"The city is {my_data['name']}, wind speed is {my_data['wind']['speed']}, the temperature is {my_data['main']['temp']} \
humidity is {my_data['main']['humidity']} and pressure is {my_data['main']['pressure']}.")

else:
    print(response.status_code)

# 3.	Task: JSON Modification
#  .	Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json
def load_books():
    try:
        with open("books.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open("books.json", "w") as f:
        json.dump(books,f, indent=4)

def add_book():
    books = load_books()
    title = input("Enter the title of the book: ")
    author = input("The name of the author: ")
    isbn = input("Enter isbn: ")
    new_book = {"title": title, "author": author, "isbn": isbn}
    books.append(new_book) 
    # there is change
    save_books(books)
    print("Book added successfully.")

def update_book():
    books = load_books()
    isbn_to_update = input("Enter the isbn of the book to update: ")
    
    found = False
    for book in books:
        if book.get('isbn')== isbn_to_update:
            new_title = input("Enter new title of the book: ")
            new_author = input("The name of the author to update: ")
            book['title']=new_title if new_title else book['title']
            book['author']=new_author if new_author else book['author']

            found = True
            break
    if found:
        save_books(books)
        print("Book updated successfully!")
    else:
        print("Book is not found.")

def delete_book():
    books = load_books()
    isbn_to_delete = input("Enter isbn to delete: ")

    initial_length = len(books)
    books = [book for book in books if book['isbn'] != isbn_to_delete]

    if len(books)<initial_length:
        save_books(books)
        print("Book successfully deleted.")
    else:
        print("Book was not found.")

def display():
    books = load_books()
    if not books:
        print("No books in the library.")
        return
    for i, book in enumerate(books):
        print(f"\n--- Book {i+1} ---")
        for key, value in book.items():
            print(f"{key.capitalize()}: {value}")

def main_menu():
    while True:
        print("\n === Book Management System ===")
        print("1. Add Book.")
        print("2. Update Book.")
        print("3. Delete Book.")
        print("4. Display Book.")
        print("5. Exit.")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()

# 4.	Task: Movie Recommendation System
#  .	Use this url http://www.omdbapi.com/ to fetch information about movies.

# i.	Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

API_KEY = "861584ad"
BASE_URL = "http://www.omdbapi.com/"

def search_movies(keyword):
    """Search movies by keyword (step 1)."""
    response = requests.get(f"{BASE_URL}?s={keyword}&apikey={API_KEY}")
    data = response.json()
    return data.get("Search", [])

def get_movie_details(imdb_id):
    """Get detailed movie info (step 2)."""
    response = requests.get(f"{BASE_URL}?i={imdb_id}&apikey={API_KEY}")
    return response.json()

def recommend_movie_by_genre(genre):
    """Find movies of a given genre and recommend one randomly."""
   
    movies = search_movies("love")  

 
    genre_matches = []
    for m in movies:
        details = get_movie_details(m["imdbID"])
        if "Genre" in details and genre.lower() in details["Genre"].lower():
            genre_matches.append(details)

    if not genre_matches:
        print(f"No movies found for genre: {genre}")
        return

    choice = random.choice(genre_matches)
    print(f"\n🎬 Recommended {genre} movie:")
    print(f"Title: {choice['Title']}")
    print(f"Year: {choice['Year']}")
    print(f"Genre: {choice['Genre']}")
    print(f"Plot: {choice['Plot']}")


user_genre = input("Enter a movie genre (e.g. Comedy, Action, Drama): ")
recommend_movie_by_genre(user_genre)

