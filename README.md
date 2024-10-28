**School Management System**

A comprehensive database management system for handling various aspects of a school, including students, teachers, subjects, classes, and grades. This project demonstrates a structured approach to managing school-related data and allows administrators to perform operations like adding new entries, updating records, and running queries to understand relationships between data entities.

**Table of Contents**
Introduction
Database Schema
Data Insertion
Queries
Setup Instructions
Usage
Results
Differences: CRUD vs. Non-CRUD Approach
License

**Introduction**
This project aims to provide a structured and efficient way to manage school data. It includes tables for students, teachers, subjects, classes, and grades, along with sample data insertion and example queries to demonstrate the relationships between tables.

**Database Schema**
The database consists of the following tables:
Students - Stores information about each student.
Subjects - Contains details about subjects taught in school.
Teachers - Includes information on teachers.
Classes - Holds data about class levels and schedules.
Grades - Stores grade records for students.
Enrollments - Manages the relationship between students and classes.
The schema illustrates these relationships and demonstrates how data flows between each entity.

**Database Schema Diagrams**

![Screenshot 2024-10-28 222302](https://github.com/user-attachments/assets/a25e1be8-3ad7-4513-af66-4f2a747ff183)

**Entity Relationships**

Students and Classes: Linked via the Enrollments table to manage which students are enrolled in which classes.
Teachers and Subjects: Connected to show which teacher instructs a given subject.

**Data Insertion**

Sample data has been added to demonstrate the functionality of the system, including:

Student Information: Basic details such as names, classes, and enrollment status.
Teacher Information: Names and subjects each teacher specializes in.
Grades: Demonstrates student performance in each enrolled class.

**Queries**

Example queries to demonstrate table relationships and data retrieval include:

1)Select all Teachers with their respective Subjects:

SELECT Teachers.FirstName, Teachers.LastName, Subjects.SubjectName
FROM Teachers
JOIN Subjects ON Teachers.SubjectID = Subjects.SubjectID;

2)Select all Students with their respective Classes:

SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Classes ON Enrollments.ClassID = Classes.ClassID;

**Setup Instructions**

Clone the Repository:

git clone https://github.com/YourUsername/School_Management_System.git

Database Setup:

Create a new database in your SQL environment.
Run the provided SQL scripts to set up tables and populate them with sample data.

Modify Connection Details:

Update any database connection details in your SQL file or project settings if required.

**Usage**
Run SQL Scripts: Execute the SQL scripts provided to initialize the database, insert sample data, and set up relationships.
Execute Sample Queries: Use the queries provided in this README to view data and test relationships between tables.
Modify the Project: Customize tables, fields, and relationships as needed for your specific requirements.

![Screenshot 2024-08-02 164710](https://github.com/user-attachments/assets/6d9dd8be-e779-429b-95a7-bafee054e2ea)

![Screenshot 2024-08-02 164718](https://github.com/user-attachments/assets/3b19b4f0-6954-41a2-a5d5-a583809a4b42)

![Screenshot 2024-08-02 164730](https://github.com/user-attachments/assets/793c8a9f-7f83-429a-8151-c84299483cd1)

![Screenshot 2024-08-02 164740](https://github.com/user-attachments/assets/6ab69087-8001-4962-9627-deae85058bf7)

![Screenshot 2024-08-02 164749](https://github.com/user-attachments/assets/00536dda-9915-4ddf-bd46-51c153a24a71)

![Screenshot 2024-08-02 164759](https://github.com/user-attachments/assets/808cc164-2782-4f0e-9016-0fbecf7f604a)

#Data Insertion:
Sample data has been inserted into the tables to demonstrate the functionality of the system. The data includes students, subjects, teachers, classes, enrollments, and grades.

#Queries:
Sample queries to demonstrate the relationships between tables:
            1)**Select all Teachers with their respective Subjects:**
                    SELECT Teachers.FirstName, Teachers.LastName, Subjects.SubjectName
                    FROM Teachers
                    JOIN Subjects ON Teachers.SubjectID = Subjects.SubjectID;
            2)**Select all Students with their respective Classes:**
                    SELECT Students.FirstName, Students.LastName, Classes.ClassName
                    FROM Students
                    JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
                    JOIN Classes ON Enrollments.ClassID = Classes.ClassID;
**Usage**:
Use the provided SQL scripts to create the database, tables, and insert sample data.
Run the example queries to see how data is related and retrieved from different tables.
Modify the scripts as per your requirements.

**Results**:

**Student Table**:

![Screenshot 2024-08-02 160201](https://github.com/user-attachments/assets/041a9af0-f5a3-4c5b-8e36-6744628e7d05)

**Teacher Table**:

![Screenshot 2024-08-02 155710](https://github.com/user-attachments/assets/148dc5c2-4cd5-4258-bc6e-ae7ce0fa872f)

**Class Table**:

![Screenshot 2024-08-02 160540](https://github.com/user-attachments/assets/403c4350-ca73-4175-b405-523111ab766a)

**Grade Table**:

![Screenshot 2024-08-02 161948](https://github.com/user-attachments/assets/2d61bd2a-e638-4778-8aa4-66e4d47a3815)

**Enrollments Table**:

![Screenshot 2024-08-02 162637](https://github.com/user-attachments/assets/2ca79d59-83c0-41a0-ab1c-4bbe6ccca48e)

**Join Table of Enrollments Id and  Class Id**:

![Screenshot 2024-08-02 162007](https://github.com/user-attachments/assets/262c51fe-4312-42c1-ac2c-3ad2f52eebdc)

**Join Table of Teacher Id and Subject Id** :

![Screenshot 2024-08-02 162415](https://github.com/user-attachments/assets/fea40585-80d2-4476-9c29-4534b7237dd7)

**Differences: CRUD vs. Non-CRUD Approach**

The School Management System can be implemented with both CRUD operations and a simpler, non-CRUD model. Here’s a comparison:

**CRUD Approach**

The CRUD approach allows users to Create, Read, Update, and Delete records, enabling dynamic data management for adding students, updating grades, or deleting outdated information.

CRUD Examples:

-- Add new student
INSERT INTO Students (FirstName, LastName) VALUES ('Jane', 'Doe');

-- View all students
SELECT * FROM Students;

-- Update a student’s class
UPDATE Enrollments SET ClassID = 2 WHERE StudentID = 1;

-- Delete a student record
DELETE FROM Students WHERE StudentID = 1;

**Non-CRUD Approach**

The non-CRUD model limits users to read-only access, meaning the data remains static after initial setup. This approach focuses on:

Pre-defined Data: Data is initially loaded and not updated frequently.
Read-Only Access: Users can only run SELECT queries to view data without modifying it.

Non-CRUD Example Queries:

-- View students with their classes
SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Classes ON Enrollments.ClassID = Classes.ClassID;

**Key Differences**

![Screenshot 2024-10-28 223118](https://github.com/user-attachments/assets/a5ab1740-3b57-4ef4-bf07-9b4b7da6e6ab)

**Images of the CRUD operations output:**



