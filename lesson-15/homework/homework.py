# Review Exercises
# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

with sqlite3.connect("database_new.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("""
        CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        Age INT
        );"""
    )

# 2. Populate your new table with the following values:

# Name	Species	Age
# Benjamin Sisko	Human	40
# Jadzia Dax	Trill	300
# Kira Nerys	Bajoran	29

    values = (
        ('Benjamin', 'Sisko	Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys','Bajoran', 29),
    )

    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values) 
# 3. Update the Name of Jadzia Dax to be Ezri Dax
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# 4. Display the Name and Age of everyone in the table classified as Bajoran.
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)
