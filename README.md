# School_Management_System

School Management System
A comprehensive database management system for handling various aspects of a school, including students, teachers, subjects, classes, and grades.

**Table of Contents**
Introduction
Database Schema
Data Insertion
Queries
Setup Instructions
Usage
License

#Introduction:
This project aims to provide a structured and efficient way to manage school data. It includes tables for students, teachers, subjects, classes, and grades, along with sample data insertion and example queries to demonstrate the relationships between the tables.

Database Schema:
The database consists of the following tables:
      1)Students
      2)Subjects
      3)Teachers
      4)Classes
      5)Grades
      6)Enrollments
      


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








