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

![Screenshot 2024-08-02 135731](https://github.com/user-attachments/assets/9820ebfe-8014-46ff-b625-9e4961797854)

![Screenshot 2024-08-02 135758](https://github.com/user-attachments/assets/6160b95f-2f98-493e-ad4f-71e110b3d825)

![Screenshot 2024-08-02 135808](https://github.com/user-attachments/assets/572f8677-bb05-4216-be21-83c0924f7cfe)

![Screenshot 2024-08-02 135819](https://github.com/user-attachments/assets/6b6812c2-9efb-4261-bd2a-5db8f32210a8)

![Screenshot 2024-08-02 135829](https://github.com/user-attachments/assets/0b86608f-aa2b-4b11-b672-1ea18d86b86e)

![Screenshot 2024-08-02 154107](https://github.com/user-attachments/assets/1489b2c5-12ec-4c1a-b789-8e4394c88b54)



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

**Grades Table**:

![Screenshot 2024-08-02 160540](https://github.com/user-attachments/assets/403c4350-ca73-4175-b405-523111ab766a)


![Screenshot 2024-08-02 161948](https://github.com/user-attachments/assets/2d61bd2a-e638-4778-8aa4-66e4d47a3815)

**Join Table of Enrollments Id and  Class Id**:

![Screenshot 2024-08-02 162007](https://github.com/user-attachments/assets/262c51fe-4312-42c1-ac2c-3ad2f52eebdc)

**Join Table of Teacher Id and Subject Id** :

![Screenshot 2024-08-02 162415](https://github.com/user-attachments/assets/fea40585-80d2-4476-9c29-4534b7237dd7)


![Screenshot 2024-08-02 162637](https://github.com/user-attachments/assets/2ca79d59-83c0-41a0-ab1c-4bbe6ccca48e)








