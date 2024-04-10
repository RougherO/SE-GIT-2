import sqlite3
from tabulate import tabulate

def initialize_database():
    conn = sqlite3.connect('marks.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS marks
                 (roll_number INTEGER PRIMARY KEY, 
                  name TEXT,
                  math_marks INTEGER,
                  science_marks INTEGER,
                  english_marks INTEGER,
                  total_marks INTEGER)''')
    
    conn.commit()
    conn.close()

def add_student(roll_number, name):
    conn = sqlite3.connect('marks.db')
    c = conn.cursor()
    c.execute("INSERT INTO marks (roll_number, name) VALUES (?, ?)", (roll_number, name))
    conn.commit()
    conn.close()

def update_marks(roll_number, subject, marks):
    conn = sqlite3.connect('marks.db')
    c = conn.cursor()
    c.execute(f"UPDATE marks SET {subject}_marks = ? WHERE roll_number = ?", (marks, roll_number))
    conn.commit()
    conn.close()

def sort_database():
    conn = sqlite3.connect('marks.db')
    c = conn.cursor()
    c.execute("UPDATE marks SET total_marks = math_marks + science_marks + english_marks")
    c.execute("SELECT * FROM marks ORDER BY total_marks DESC")
    result = c.fetchall()
    conn.close()
    return result

def display_students(students):
    headers = ["Roll Number", "Name", "Math Marks", "Science Marks", "English Marks", "Total Marks"]
    print(tabulate(students, headers=headers, tablefmt="grid"))

def display_menu():
    print("\nMenu:")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. View Student Information")
    print("4. Exit")

def main():
    initialize_database()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = int(input("Enter roll number: "))
            name = input("Enter name: ")
            add_student(roll_number, name)
            print("Student added successfully.")
        elif choice == '2':
            roll_number = int(input("Enter roll number: "))
            subject = input("Enter subject (math/science/english): ")
            marks = int(input(f"Enter marks for {subject}: "))
            update_marks(roll_number, subject, marks)
            print("Marks updated successfully.")
        elif choice == '3':
            students = sort_database()
            display_students(students)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()