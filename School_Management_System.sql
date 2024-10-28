CREATE DATABASE School_Management_System;
USE School_Management_System;

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(50)
);

CREATE TABLE Subjects (
    SubjectID INT AUTO_INCREMENT PRIMARY KEY,
    SubjectName VARCHAR(50)
);

CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(50),
    SubjectID INT,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);

CREATE TABLE Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(50),
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    ClassID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);


CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    SubjectID INT,
    Grade CHAR(1),
    GradeDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);

INSERT INTO Students (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email)
VALUES 
('Aarav', 'Sharma', '2004-01-12', 'Male', '45 Gandhi Rd', '+91 9949701001', 'aarav.sharma@gmail.com'),
('Vivaan', 'Patel', '2003-02-25', 'Male', '67 Nehru St', '+91 9949701002', 'vivaan.patel@gmail.com'),
('Aditya', 'Mehta', '2005-03-30', 'Male', '89 Tagore Ln', '+91 9949701003', 'aditya.mehta@gmail.com'),
('Vihaan', 'Agarwal', '2004-04-15', 'Male', '23 Bhagat Singh Marg', '+91 9949701004', 'vihaan.agarwal@gmail.com'),
('Ayaan', 'Kumar', '2003-05-20', 'Male', '56 Bose Rd', '+91 9949701005', 'ayaan.kumar@gmail.com'),
('Arjun', 'Reddy', '2005-06-10', 'Male', '78 Sarojini Naidu St', '+91 9949701006', 'arjun.reddy@gmail.com'),
('Sai', 'Iyer', '2004-07-25', 'Male', '91 Patel Nagar', '+91 9949701007', 'sai.iyer@gmail.com'),
('Anaya', 'Singh', '2003-08-14', 'Female', '34 Lajpat Nagar', '+91 9949701008', 'anaya.singh@gmail.com'),
('Diya', 'Verma', '2005-09-05', 'Female', '12 Ambedkar Rd', '+91 9949701009', 'diya.verma@gmail.com'),
('Aarohi', 'Malhotra', '2004-10-21', 'Female', '56 Aurobindo Marg', '+91 9949701010', 'aarohi.malhotra@gmail.com'),
('Riya', 'Chopra', '2003-11-30', 'Female', '78 Tilak Rd', '+91 9949701011', 'riya.chopra@gmail.com'),
('Kiara', 'Nair', '2005-12-18', 'Female', '89 Jinnah Rd', '+91 9949701012', 'kiara.nair@gmail.com'),
('Ishaan', 'Joshi', '2004-01-07', 'Male', '23 Vivekananda Rd', '+91 9949701013', 'ishaan.joshi@gmail.com'),
('Anvi', 'Das', '2003-02-19', 'Female', '45 Tagore Park', '+91 9949701014', 'anvi.das@gmail.com'),
('Prisha', 'Chatterjee', '2005-03-12', 'Female', '67 Roy Rd', '+91 9949701015', 'prisha.chatterjee@gmail.com'),
('Arnav', 'Ghosh', '2004-04-03', 'Male', '89 Bose Park', '+91 9949701016', 'arnav.ghosh@gmail.com'),
('Kabir', 'Saxena', '2003-05-14', 'Male', '12 Subhash Marg', '+91 9949701017', 'kabir.saxena@gmail.com'),
('Aryan', 'Sinha', '2005-06-25', 'Male', '34 Patel Rd', '+91 9949701018', 'aryan.sinha@gmail.com'),
('Navya', 'Rao', '2004-07-16', 'Female', '56 Nehru St', '+91 9949701019', 'navya.rao@gmail.com'),
('Saanvi', 'Naidu', '2003-08-27', 'Female', '78 Indira Nagar', '+91 9949701020', 'saanvi.naidu@gmail.com'),
('Kavya', 'Reddy', '2005-09-18', 'Female', '89 Gandhi Nagar', '+91 9949701021', 'kavya.reddy@gmail.com'),
('Aisha', 'Menon', '2004-10-09', 'Female', '23 Nehru Rd', '+91 9949701022', 'aisha.menon@gmail.com'),
('Dev', 'Nair', '2003-11-20', 'Male', '45 Sarojini Rd', '+91 9949701023', 'dev.nair@gmail.com'),
('Reyansh', 'Mishra', '2005-12-11', 'Male', '67 Ambedkar Nagar', '+91 9949701024', 'reyansh.mishra@gmail.com'),
('Anika', 'Roy', '2004-01-22', 'Female', '78 Patel Nagar', '+91 9949701025', 'anika.roy@gmail.com'),
('Aadhya', 'Kapoor', '2003-02-13', 'Female', '89 Bose Rd', '+91 9949701026', 'aadhya.kapoor@gmail.com'),
('Shaan', 'Bhat', '2005-03-24', 'Male', '12 Gandhi Rd', '+91 9949701027', 'shaan.bhat@gmail.com'),
('Krishna', 'Rana', '2004-04-05', 'Male', '34 Subhash Marg', '+91 9949701028', 'krishna.rana@gmail.com'),
('Rishi', 'Dutta', '2003-05-16', 'Male', '56 Vivekananda Park', '+91 9949701029', 'rishi.dutta@gmail.com'),
('Nirvaan', 'Chandra', '2005-06-27', 'Male', '78 Bose St', '+91 9949701030', 'nirvaan.chandra@gmail.com');

INSERT INTO Subjects (SubjectName)
VALUES 
('Physics'),
('Chemistry'),
('Biology'),
('Maths'),
('Telugu');

INSERT INTO Teachers (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email, SubjectID)
VALUES 
('Alice', 'Johnson', '1980-03-12', 'Female', '789 Elm St', '555-8765', 'alice.johnson@gmail.com', 1),
('Bob', 'Brown', '1975-07-22', 'Male', '321 Oak Rd', '555-4321', 'bob.brown@gmail.com', 2),
('Ravi', 'Sharma', '1985-04-14', 'Male', '123 MG Road', '+91 9949701041', 'ravi.sharma@gmail.com', 3),
('Sneha', 'Patel', '1988-08-19', 'Female', '456 Nehru Street', '+91 9949701042', 'sneha.patel@gmail.com', 4),
('Anil', 'Mehta', '1979-12-05', 'Male', '789 Tagore Lane', '+91 9949701043', 'anil.mehta@gmail.com', 5),
('Kiran', 'Rao', '1982-11-21', 'Female', '101 Bose Road', '+91 9949701044', 'kiran.rao@gmail.com', 1),
('Priya', 'Singh', '1990-07-15', 'Female', '234 Ambedkar Road', '+91 9949701045', 'priya.singh@gmail.com', 2),
('Deepak', 'Kumar', '1983-09-17', 'Male', '678 Bapu Street', '+91 9949701051', 'deepak.kumar@gmail.com', 3),
('Asha', 'Nair', '1984-11-25', 'Female', '910 Gandhi Road', '+91 9949701052', 'asha.nair@gmail.com', 4),
('Sunil', 'Gupta', '1976-05-03', 'Male', '123 Subhash Lane', '+91 9949701053', 'sunil.gupta@gmail.com', 5),
('Meera', 'Shah', '1981-08-14', 'Female', '456 Patel Street', '+91 9949701054', 'meera.shah@gmail.com', 1),
('Rohan', 'Desai', '1987-01-27', 'Male', '789 Tagore Lane', '+91 9949701055', 'rohan.desai@gmail.com', 2);

select * from Teachers;
select * from Students;

select * from  Subjects;
select * from Enrollments;

INSERT INTO Classes (ClassName, TeacherID)
VALUES 
('Class 1A', 1), 
('Class 1B', 2),
('Class 2A', 3),
('Class 2B', 4),
('Class 3A', 2),
('Class 3B', 3),
('Class 4A', 1),
('Class 4B', 2),
('Class 5A', 3),
('Class 5B', 4),
('Class 6A', 5),
('Class 6B', 6),
('Class 7A', 7),
('Class 7B', 8),
('Class 8A', 9),
('Class 8B', 10),
('Class 9A', 11),
('Class 9B', 12),
('Class 10A', 1),
('Class 10B', 4);

select * from Classes;

INSERT INTO Enrollments (StudentID, ClassID, EnrollmentDate)
VALUES 
(1, 21, '2024-08-01'),
(2, 22, '2024-08-01'),
(3, 23, '2024-08-01'),
(4, 24, '2024-08-01'),
(5, 25, '2024-08-01'),
(6, 26, '2024-08-01'),
(7, 27, '2024-08-01'),
(8, 28, '2024-08-01'),
(9, 29, '2024-08-01'),
(10, 30, '2024-08-01'),
(11, 31, '2024-08-01'),
(12, 32, '2024-08-01'),
(13, 33, '2024-08-01'),
(14, 34, '2024-08-01'),
(15, 35, '2024-08-01'),
(16, 36, '2024-08-01'),
(17, 37, '2024-08-01'),
(18, 38, '2024-08-01'),
(19, 39, '2024-08-01'),
(20, 40, '2024-08-01'),
(21, 21, '2024-08-01'),
(22, 22, '2024-08-01'),
(23, 23, '2024-08-01'),
(24, 24, '2024-08-01'),
(25, 25, '2024-08-01'),
(26, 26, '2024-08-01'),
(27, 27, '2024-08-01'),
(28, 28, '2024-08-01'),
(29, 29, '2024-08-01'),
(30, 30, '2024-08-01');


INSERT INTO Grades (StudentID, SubjectID, Grade, GradeDate)
VALUES
(1, 1, 'A', '2024-06-01'),
(2, 2, 'B', '2024-06-01'),
(3, 3, 'C', '2024-06-01'),
(4, 4, 'A', '2024-06-01'),
(5, 5, 'B', '2024-06-01'),
(6, 1, 'C', '2024-06-01'),
(7, 2, 'A', '2024-06-01'),
(8, 3, 'B', '2024-06-01'),
(9, 4, 'C', '2024-06-01'),
(10, 5, 'A', '2024-06-01'),
(11, 1, 'B', '2024-06-01'),
(12, 2, 'C', '2024-06-01'),
(13, 3, 'A', '2024-06-01'),
(14, 4, 'B', '2024-06-01'),
(15, 5, 'C', '2024-06-01'),
(16, 1, 'A', '2024-06-01'),
(17, 2, 'B', '2024-06-01'),
(18, 3, 'C', '2024-06-01'),
(19, 4, 'A', '2024-06-01'),
(20, 5, 'B', '2024-06-01'),
(21, 1, 'C', '2024-06-01'),
(22, 2, 'A', '2024-06-01'),
(23, 3, 'B', '2024-06-01'),
(24, 4, 'C', '2024-06-01'),
(25, 5, 'A', '2024-06-01'),
(26, 1, 'B', '2024-06-01'),
(27, 2, 'C', '2024-06-01'),
(28, 3, 'A', '2024-06-01'),
(29, 4, 'B', '2024-06-01'),
(30, 5, 'C', '2024-06-01'),
(30, 1, 'A', '2024-06-01'),
(22, 2, 'B', '2024-06-01'),
(23, 3, 'C', '2024-06-01'),
(24, 4, 'A', '2024-06-01'),
(25, 5, 'B', '2024-06-01'),
(26, 1, 'C', '2024-06-01'),
(27, 2, 'A', '2024-06-01'),
(28, 3, 'B', '2024-06-01'),
(29, 4, 'C', '2024-06-01'),
(30, 5, 'A', '2024-06-01'),
(11, 1, 'B', '2024-06-01'),
(12, 2, 'C', '2024-06-01'),
(13, 3, 'A', '2024-06-01'),
(14, 4, 'B', '2024-06-01'),
(15, 5, 'C', '2024-06-01'),
(16, 1, 'A', '2024-06-01'),
(17, 2, 'B', '2024-06-01'),
(18, 3, 'C', '2024-06-01'),
(19, 4, 'A', '2024-06-01'),
(30, 5, 'B', '2024-06-01'),
(11, 1, 'C', '2024-06-01'),
(2, 2, 'A', '2024-06-01'),
(3, 3, 'B', '2024-06-01'),
(4, 4, 'C', '2024-06-01'),
(5, 5, 'A', '2024-06-01'),
(6, 1, 'B', '2024-06-01'),
(7, 2, 'C', '2024-06-01'),
(8, 3, 'A', '2024-06-01'),
(9, 4, 'B', '2024-06-01'),
(4, 5, 'C', '2024-06-01'),
(1, 1, 'A', '2024-06-01'),
(12, 2, 'B', '2024-06-01'),
(13, 3, 'C', '2024-06-01'),
(14, 4, 'A', '2024-06-01'),
(15, 5, 'B', '2024-06-01');


SELECT * FROM Grades;

SELECT Students.FirstName, Students.LastName, Classes.ClassName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Classes ON Enrollments.ClassID = Classes.ClassID;

SELECT Teachers.FirstName, Teachers.LastName, Subjects.SubjectName
FROM Teachers
JOIN Subjects ON Teachers.SubjectID = Subjects.SubjectID;


