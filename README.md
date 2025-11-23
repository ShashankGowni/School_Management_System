<<<<<<< HEAD
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
=======
# 🏫 School Management System

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red)

**A comprehensive database management system for schools, managing students, teachers, subjects, classes, enrollments, and grades with full CRUD operations.**

Built with Flask, Python, MySQL, and a responsive web interface.

---

## 📚 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- ✅ **Student Management** - Add, edit, view, and delete student records
- ✅ **Teacher Management** - Manage teachers and subject assignments
- ✅ **Subject & Class Management** - Organize academic subjects and class schedules
- ✅ **Enrollment System** - Link students to classes with enrollment tracking
- ✅ **Grade Management** - Record and track student performance
- ✅ **Relationship Queries** - Complex joins across Students, Teachers, Classes, and Grades
- ✅ **Responsive Web Interface** - Works on desktop, tablet, and mobile
- ✅ **Full CRUD Operations** - Create, Read, Update, Delete for all entities

---

## 📸 Screenshots

### Database Schema

![Database Schema](https://github.com/user-attachments/assets/a25e1be8-3ad7-4513-af66-4f2a747ff183)

### Data Tables

**Students Table**
![Students](https://github.com/user-attachments/assets/041a9af0-f5a3-4c5b-8e36-6744628e7d05)

**Teachers Table**
![Teachers](https://github.com/user-attachments/assets/148dc5c2-4cd5-4258-bc6e-ae7ce0fa872f)

**Classes Table**
![Classes](https://github.com/user-attachments/assets/403c4350-ca73-4175-b405-523111ab766a)

**Grades Table**
![Grades](https://github.com/user-attachments/assets/2d61bd2a-e638-4778-8aa4-66e4d47a3815)

**Enrollments Table**
![Enrollments](https://github.com/user-attachments/assets/2ca79d59-83c0-41a0-ab1c-4bbe6ccca48e)

### Join Queries

**Students + Classes Join**
![Join 1](https://github.com/user-attachments/assets/262c51fe-4312-42c1-ac2c-3ad2f52eebdc)

**Teachers + Subjects Join**
![Join 2](https://github.com/user-attachments/assets/fea40585-80d2-4476-9c29-4534b7237dd7)

### CRUD Operations

![CRUD 1](https://github.com/user-attachments/assets/683a7019-c208-429b-be90-e3c7ec5315d6)
![CRUD 2](https://github.com/user-attachments/assets/12fea58f-25ba-4c47-8ece-900567e962b8)
![CRUD 3](https://github.com/user-attachments/assets/36ed0cf5-467d-4e40-86fd-ef92aba22ceb)

### CRUD vs Non-CRUD Comparison

![Comparison](https://github.com/user-attachments/assets/a5ab1740-3b57-4ef4-bf07-9b4b7da6e6ab)

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Flask** | Web framework |
| **MySQL** | Relational database |
| **mysql-connector-python** | Database driver |
| **python-dotenv** | Environment variables |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Page structure |
| **CSS3** | Styling |
| **Jinja2** | Template engine |
| **JavaScript** | Dynamic interactions |

---

## 🗄️ Database Schema

### Tables

- **Students** - Student information (StudentID, FirstName, LastName, DateOfBirth, Email)
- **Teachers** - Teacher details (TeacherID, FirstName, LastName, SubjectID, Email)
- **Subjects** - Academic subjects (SubjectID, SubjectName, Description)
- **Classes** - Class schedules (ClassID, ClassName, TeacherID, Schedule)
- **Enrollments** - Student-Class mapping (EnrollmentID, StudentID, ClassID, EnrollmentDate)
- **Grades** - Student performance (GradeID, StudentID, SubjectID, Grade, Date)

### Key Relationships

- **Students ↔ Classes** - Many-to-many via Enrollments table
- **Teachers ↔ Subjects** - One-to-many relationship
- **Students ↔ Grades** - One-to-many relationship

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- MySQL 8.0+
- Git

### Setup Steps

**1. Clone Repository**

```bash
git clone https://github.com/ShashankGowni/School_Management_System.git
cd School_Management_System
```
**2. Create Virtual Environment**
```bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
**3. Install Dependencies**
```bash

pip install -r requirements.txt
```
**4. Setup Database**
Create database:

```SQL

CREATE DATABASE school_management;
USE school_management;
```
**Run schema:**

```bash

mysql -u root -p school_management < create_school_management_tables.sql
```
**Load sample data (optional):**

```bash

mysql -u root -p school_management < School_Management_System.sql
```
**5. Configure Environment**

**Create .env file:**

```env```
```
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=school_management
SECRET_KEY=your_secret_key_here
```

**Generate secret key:**

```Python

import secrets
print(secrets.token_hex(16))
```
**6. Run Application**
```bash

python app.py
```
**🌐 Open browser: http://localhost:5000**

## 🎯 Usage
**Managing Students**
- Add Student: Click "Add Student" → Fill form → Submit
- Edit Student: Click student name → Modify fields → Save
- Delete Student: Click "Delete" → Confirm

**Enrolling Students**

- Go to Enrollments page
- Select student and class
- Choose enrollment date
- Submit
- Recording Grades
- Go to Grades page
- Select student and subject
- Enter grade (A-F)
- Submit
## Sample Queries

**Students with their classes:**

```SQL

SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Classes ON Enrollments.ClassID = Classes.ClassID;
Teachers with subjects:
```
```SQL
>>>>>>> 65c2833 (Initial commit for School Management System project)

SELECT Teachers.FirstName, Teachers.LastName, Subjects.SubjectName
FROM Teachers
JOIN Subjects ON Teachers.SubjectID = Subjects.SubjectID;
<<<<<<< HEAD

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

![Screenshot 2024-10-28 225053](https://github.com/user-attachments/assets/683a7019-c208-429b-be90-e3c7ec5315d6)

![Screenshot 2024-10-28 135619](https://github.com/user-attachments/assets/12fea58f-25ba-4c47-8ece-900567e962b8)

![Screenshot 2024-10-28 223504](https://github.com/user-attachments/assets/36ed0cf5-467d-4e40-86fd-ef92aba22ceb)

![Screenshot 2024-10-28 223532](https://github.com/user-attachments/assets/8dde54cb-78d1-4903-9e97-e6e5deef70a7)

![Screenshot 2024-10-28 223546](https://github.com/user-attachments/assets/12d6a0b5-e9eb-4b52-846a-73bdff8c9487)

![Screenshot 2024-10-28 223557](https://github.com/user-attachments/assets/f8f72950-7647-4e44-aca8-318d4006af68)

![Screenshot 2024-10-28 223616](https://github.com/user-attachments/assets/0d4b7da4-a74b-4525-bf22-88939ba90b64)

=======
```
📁 Project Structure
```text

School_Management_System/
├── app.py                              # Main Flask app
├── school_management_system.py         # Core logic
├── create_school_management_tables.sql # Database schema
├── School_Management_System.sql        # Sample data
├── requirements.txt                    # Dependencies
├── .env                               # Config (not tracked)
├── .gitignore                         # Git ignore rules
├── templates/                         # HTML templates
├── static/                            # CSS, JS, images
└── venv/                              # Virtual env (not tracked)
```

## 🐛 Troubleshooting
Database Connection Error

**Check MySQL is running:**

```bash

mysql --version
```
**Verify .env credentials:**

```env```
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_management
Module Not Found
```
**Reinstall dependencies:**

```bash

pip install -r requirements.txt
```
**Port Already in Use**
Change port in app.py:

```Python

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

## 📝 License
© 2025 Gowni Shashank. All Rights Reserved.

This software is proprietary and confidential. See the LICENSE file for complete terms.

License Summary
- ✅ Viewable for portfolio/demonstration purposes only
- ❌ No permission to use, copy, modify, or distribute
- ❌ Commercial use strictly prohibited without written permission
- 💼 For licensing inquiries: shashankgowni09@gmail.com
This project is shared publicly to showcase my development capabilities.

## 🙏 Acknowledgments
- Flask - Web framework
- MySQL - Database management
- Python - Programming language
- Jinja2 - Template engine

## 📬 Contact
Gowni Shashank

- 📧 Email: shashankgowni09@gmail.com
- 💼 LinkedIn: linkedin.com/in/shashankgowni
- 🐙 GitHub: @ShashankGowni

Open to collaboration on interesting projects.

**Created with 💻 by Gowni Shashank • January 2025 🌍**
>>>>>>> 65c2833 (Initial commit for School Management System project)
