1)Students Table:
  
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    PhoneNumber VARCHAR(15),
    Email VARCHAR(50)
);

2)Teachers Table:

CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Subject VARCHAR(50)
);

3)Courses Table:

CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(100),
    Description TEXT,
);

4)Enrollments Table:

CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

5)Grades Table:

CREATE TABLE Grades (
    GradeID INT AUTO_INCREMENT PRIMARY KEY,
    EnrollmentID INT,
    Grade VARCHAR(2),
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID)
);
