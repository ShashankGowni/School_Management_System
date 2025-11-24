# 🏫 School Management System

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red)

**A Flask-based school management system with student, teacher, class, and grade administration featuring full CRUD operations and MySQL database.**

Live Demo: [school-management-system-atyl.onrender.com](https://school-management-system-atyl.onrender.com)

---

## 📚 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Installation](#-installation)
- [Usage](#-usage)
- [CRUD Operations](#-crud-operations)
- [Project Structure](#-project-structure)
- [Deployment](#-deployment)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- ✅ **Student Management** - Add, edit, view, and delete student records
- ✅ **Teacher Management** - Manage teachers and subject assignments
- ✅ **Subject & Class Management** - Organize academic subjects and class schedules
- ✅ **Enrollment System** - Link students to classes with enrollment tracking
- ✅ **Grade Management** - Record and track student performance
- ✅ **Relationship Queries** - Complex SQL joins across multiple tables
- ✅ **Responsive Web Interface** - Mobile-friendly design
- ✅ **Full CRUD Operations** - Create, Read, Update, Delete for all entities
- ✅ **Cloud Deployed** - Live on Render with MySQL database

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
| **Flask** | Lightweight web framework |
| **MySQL** | Relational database |
| **mysql-connector-python** | Database driver |
| **python-dotenv** | Environment variable management |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Page structure |
| **CSS3** | Styling and responsive design |
| **Jinja2** | Flask template engine |
| **JavaScript** | Dynamic interactions |

### Deployment
- **Render** - Cloud hosting platform
- **MySQL Database** - Cloud-hosted relational database

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

- Python 3.8 or higher
- MySQL 8.0 or higher
- Git

### Local Setup

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
**Run schema script:**

```bash

mysql -u root -p school_management < create_school_management_tables.sql
```
**Load sample data (optional):**

```bash

mysql -u root -p school_management < School_Management_System.sql
```
**5. Configure Environment**

Create .env file in project root:

```env``
```
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=school_management
SECRET_KEY=your_secret_key_here
```
**Generate secret key in Python:**

```Python

import secrets
print(secrets.token_hex(16))
```
**6. Run Application**
```bash

python app.py
```
```🌐 Access: http://localhost:5000```

## 🎯 Usage
Managing Students

**Add Student:**

- Click "Add Student" button
- Fill in: First Name, Last Name, Date of Birth, Email
- Click "Submit"

**Edit Student:**

Click on student name in table
Modify desired fields
Click "Save Changes"

**Delete Student:**

- Click "Delete" button
- Confirm deletion
- Enrolling Students in Classes
- Navigate to Enrollments page
- Select student from dropdown
- Select class from dropdown
- Choose enrollment date
- Click "Submit"
- Recording Grades
- Go to Grades page
- Select student
- Select subject
- Enter grade (A, B, C, D, F)
- Add date
- Click "Submit"

## 🔄 CRUD Operations
**Example SQL Queries**
View students with their classes:

```SQL

SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Classes ON Enrollments.ClassID = Classes.ClassID;
```
**View teachers with subjects:**

```SQL

SELECT Teachers.FirstName, Teachers.LastName, Subjects.SubjectName
FROM Teachers
JOIN Subjects ON Teachers.SubjectID = Subjects.SubjectID;
```
**Add new student:**

```SQL

INSERT INTO Students (FirstName, LastName, DateOfBirth, Email)
VALUES ('John', 'Doe', '2005-03-15', 'john.doe@school.com');
```
**Update student email:**

```SQL

UPDATE Students 
SET Email = 'newemail@school.com' 
WHERE StudentID = 1;
```
**Delete enrollment:**

```SQL

DELETE FROM Enrollments WHERE EnrollmentID = 5;
```
📁 Project Structure
```text

School_Management_System/
├── app.py                              # Main Flask application
├── school_management_system.py         # Core business logic
├── create_school_management_tables.sql # Database schema
├── School_Management_System.sql        # Sample data
├── requirements.txt                    # Python dependencies
├── .env                               # Environment variables (not tracked)
├── .gitignore                         # Git ignore rules
├── LICENSE                            # Proprietary license
├── templates/                         # HTML templates
│   ├── base.html
│   ├── students.html
│   ├── teachers.html
│   └── ...
├── static/                            # CSS, JS, images
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── venv/                              # Virtual environment (not tracked)
```

## 🚀 Deployment
This project is deployed on Render at: school-management-system-atyl.onrender.com

- Deploy Your Own
- Fork this repository
- Create account on Render
- Create new MySQL database on Render
- Create new Web Service
- Connect GitHub repository

**Set environment variables:**

- DB_HOST
- DB_USER
- DB_PASSWORD
- DB_NAME
- SECRET_KEY
- Deploy!

## 🐛 Troubleshooting

Database Connection Error

**Verify MySQL is running:**

```bash

mysql --version
```
**Check credentials in .env:**

```env

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_management
```
## Module Not Found Error

**Reinstall dependencies:**

```Bash

pip install -r requirements.txt
```
**Port Already in Use**

Change port in app.py:

```Python

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

**Tables Don't Exist**
Re-run schema script:

```Bash

mysql -u root -p school_management < create_school_management_tables.sql
```

## 📝 License
© 2025 Gowni Shashank. All Rights Reserved.

This software is proprietary and confidential. See the LICENSE file for complete terms.

**License Summary**
- ✅ Viewable for portfolio/demonstration purposes only
- ❌ No permission to use, copy, modify, or distribute
- ❌ Commercial use strictly prohibited without written permission
- 💼 For licensing inquiries: shashankgowni09@gmail.com
This project is shared publicly to showcase my development capabilities.

## 🙏 Acknowledgments
- Flask - Lightweight Python web framework
- MySQL - Reliable relational database
- Render - Cloud hosting platform
- Python - Programming language
- Jinja2 - Template engine

## 📬 Contact
Gowni Shashank

- 📧 Email: shashankgowni09@gmail.com
- 💼 LinkedIn: linkedin.com/in/shashankgowni
- 🐙 GitHub: @ShashankGowni

Open to collaboration on interesting projects.

**Created with 💻 by Gowni Shashank • January 2025 🌍**