import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Get the credentials from the environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",      # Change if necessary
    user=db_user,         # Use the username from .env
    password=db_password,  # Use the password from .env
    database=db_name       # Use the database name from .env
)

cursor = db.cursor()

# Function to add a student
def add_student(first_name, last_name, dob, email, phone):
    try:
        cursor.execute("""
            INSERT INTO students (first_name, last_name, dob, email, phone)
            VALUES (%s, %s, %s, %s, %s)
        """, (first_name, last_name, dob, email, phone))
        db.commit()
        print("Student added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        print("Students:")
        for student in students:
            print(student)
    else:
        print("No students found.")

# Function to update a student's details
def update_student(student_id, first_name, last_name, dob, email, phone):
    try:
        cursor.execute("""
            UPDATE students
            SET first_name = %s, last_name = %s, dob = %s, email = %s, phone = %s
            WHERE student_id = %s
        """, (first_name, last_name, dob, email, phone, student_id))
        if cursor.rowcount > 0:
            db.commit()
            print("Student details updated successfully.")
        else:
            print("No student found with that ID.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to delete a student
def delete_student(student_id):
    try:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        if cursor.rowcount > 0:
            db.commit()
            print("Student deleted successfully.")
        else:
            print("No student found with that ID.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to enroll a student in a course
def enroll_student(student_id, course_id):
    try:
        if is_already_enrolled(student_id, course_id):
            print("This student is already enrolled in this course.")
            return
        
        cursor.execute("""
            INSERT INTO enrollments (student_id, course_id, enrollment_date)
            VALUES (%s, %s, CURDATE())
        """, (student_id, course_id))
        db.commit()
        print("Student enrolled successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to check if a student is already enrolled in a course
def is_already_enrolled(student_id, course_id):
    cursor.execute("""
        SELECT * FROM enrollments
        WHERE student_id = %s AND course_id = %s
    """, (student_id, course_id))
    return cursor.fetchone() is not None

# Function to view all courses (assuming you have a courses table)
def view_courses():
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    if courses:
        print("Courses:")
        for course in courses:
            print(course)
    else:
        print("No courses found.")

# Main menu for the application
def main_menu():
    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Enroll Student in Course")
        print("6. View Courses")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            add_student(first_name, last_name, dob, email, phone)

        elif choice == '2':
            view_students()

        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            dob = input("Enter new date of birth (YYYY-MM-DD): ")
            email = input("Enter new email: ")
            phone = input("Enter new phone number: ")
            update_student(student_id, first_name, last_name, dob, email, phone)

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            enroll_student(student_id, course_id)

        elif choice == '6':
            view_courses()

        elif choice == '7':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()

# Close the connection
cursor.close()
db.close()
