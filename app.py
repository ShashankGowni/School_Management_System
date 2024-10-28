import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            print("Database connection successful.")
        return connection
    except Error as e:
        print(f"Error: {e}")
        flash("Database connection failed.")
        return None

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role')  # Use .get() to avoid KeyError if role is missing
        hashed_password = generate_password_hash(password)

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", 
                               (username, hashed_password, role))
                connection.commit()
                flash('Registration successful!')
                return redirect(url_for('login'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['role'] = user['role']
                flash('Login successful!')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.')
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    connection = create_connection()
    cursor = connection.cursor()

    # Get total number of students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Get total number of teachers
    cursor.execute("SELECT COUNT(*) FROM teachers")
    total_teachers = cursor.fetchone()[0]

    # Get total number of courses
    cursor.execute("SELECT COUNT(*) FROM courses")
    total_courses = cursor.fetchone()[0]

    # Get total number of enrollments
    cursor.execute("SELECT COUNT(*) FROM enrollments")
    total_enrollments = cursor.fetchone()[0]

    # Get total number of grades
    cursor.execute("SELECT COUNT(*) FROM grades")
    total_grades = cursor.fetchone()[0]

    cursor.close()
    return render_template('dashboard.html', 
                           total_students=total_students,
                           total_teachers=total_teachers,
                           total_courses=total_courses,
                           total_enrollments=total_enrollments,
                           total_grades=total_grades)

# CRUD operations for students
@app.route('/students')
def view_students():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('view_students.html', students=students)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO students (first_name, last_name, dob, email, phone) VALUES (%s, %s, %s, %s, %s)", 
                               (first_name, last_name, dob, email, phone))
                connection.commit()
                flash('Student added successfully!')
                return redirect(url_for('view_students'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('add_student.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        student = cursor.fetchone()
        if not student:
            flash("Student not found.")
            return redirect(url_for('view_students'))

        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            email = request.form['email']
            phone = request.form['phone']

            try:
                cursor.execute("UPDATE students SET first_name = %s, last_name = %s, dob = %s, email = %s, phone = %s WHERE id = %s", 
                               (first_name, last_name, dob, email, phone, id))
                connection.commit()
                flash('Student updated successfully!')
                return redirect(url_for('view_students'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            connection.commit()
            flash('Student deleted successfully!')
        except Error as e:
            flash(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('view_students'))

# CRUD operations for teachers
@app.route('/teachers')
def view_teachers():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM teachers")
        teachers = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('view_teachers.html', teachers=teachers)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))

@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')  # Make sure 'subject' is included in the form

        print(request.form)  # Debugging line to see what data is received

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO teachers (first_name, last_name, email, phone, subject) VALUES (%s, %s, %s, %s, %s)", 
                               (first_name, last_name, email, phone, subject))
                connection.commit()
                flash('Teacher added successfully!')
                return redirect(url_for('view_teachers'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('add_teacher.html')

@app.route('/edit_teacher/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM teachers WHERE id = %s", (id,))
        teacher = cursor.fetchone()
        if not teacher:
            flash("Teacher not found.")
            return redirect(url_for('view_teachers'))

        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            subject = request.form['subject']
            email = request.form['email']
            phone = request.form['phone']

            try:
                cursor.execute("UPDATE teachers SET first_name = %s, last_name = %s, subject = %s, email = %s, phone = %s WHERE id = %s", 
                               (first_name, last_name, subject, email, phone, id))
                connection.commit()
                flash('Teacher updated successfully!')
                return redirect(url_for('view_teachers'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('edit_teacher.html', teacher=teacher)

@app.route('/delete_teacher/<int:id>', methods=['POST'])
def delete_teacher(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM teachers WHERE id = %s", (id,))
            connection.commit()
            flash('Teacher deleted successfully!')
        except Error as e:
            flash(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('view_teachers'))

# CRUD operations for courses
@app.route('/courses')
def view_courses():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('view_courses.html', courses=courses)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        course_description = request.form['course_description']

        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO courses (course_name, course_description) VALUES (%s, %s)", 
                               (course_name, course_description))
                connection.commit()
                flash('Course added successfully!')
                return redirect(url_for('view_courses'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('add_course.html')

@app.route('/edit_course/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses WHERE id = %s", (id,))
        course = cursor.fetchone()
        if not course:
            flash("Course not found.")
            return redirect(url_for('view_courses'))

        if request.method == 'POST':
            course_name = request.form['course_name']
            course_description = request.form['course_description']

            try:
                cursor.execute("UPDATE courses SET course_name = %s, course_description = %s WHERE id = %s", 
                               (course_name, course_description, id))
                connection.commit()
                flash('Course updated successfully!')
                return redirect(url_for('view_courses'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
    return render_template('edit_course.html', course=course)

@app.route('/delete_course/<int:id>', methods=['POST'])
def delete_course(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM courses WHERE id = %s", (id,))
            connection.commit()
            flash('Course deleted successfully!')
        except Error as e:
            flash(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('view_courses'))

# Enrollment management
@app.route('/enrollments')
def view_enrollments():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT enrollments.id, students.first_name, students.last_name, courses.course_name
            FROM enrollments
            JOIN students ON enrollments.student_id = students.id
            JOIN courses ON enrollments.course_id = courses.id
        """)
        enrollments = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('view_enrollments.html', enrollments=enrollments)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))

@app.route('/add_enrollment', methods=['GET', 'POST'])
def add_enrollment():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()
        
        if request.method == 'POST':
            student_id = request.form['student_id']
            course_id = request.form['course_id']
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)", 
                               (student_id, course_id))
                connection.commit()
                flash('Enrollment added successfully!')
                return redirect(url_for('view_enrollments'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
        
        return render_template('add_enrollment.html', students=students, courses=courses)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))
    
@app.route('/edit_enrollment/<int:id>', methods=['GET', 'POST'])
def edit_enrollment(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)

        # Fetch the existing enrollment
        cursor.execute("""
            SELECT * FROM enrollments WHERE id = %s
        """, (id,))
        enrollment = cursor.fetchone()

        # Fetch all students and courses
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()

        if request.method == 'POST':
            student_id = request.form['student_id']
            course_id = request.form['course_id']
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    UPDATE enrollments SET student_id = %s, course_id = %s WHERE id = %s
                """, (student_id, course_id, id))
                connection.commit()
                flash('Enrollment updated successfully!')
                return redirect(url_for('view_enrollments'))
            except Error as e:
                flash(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

        return render_template('edit_enrollment.html', enrollment=enrollment, students=students, courses=courses)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))
    
@app.route('/delete_enrollment/<int:id>', methods=['POST'])
def delete_enrollment(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM enrollments WHERE id = %s", (id,))
            connection.commit()
            flash('Enrollment deleted successfully!')
        except Error as e:
            flash(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    return redirect(url_for('view_enrollments'))

@app.route('/grades')
def view_grades():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT g.id, s.first_name, s.last_name, c.course_name, g.grade
            FROM grades g
            JOIN students s ON g.student_id = s.id
            JOIN courses c ON g.course_id = c.id
        """)
        grades = cursor.fetchall()
        cursor.close()
        return render_template('view_grades.html', grades=grades)
    else:
        flash('Database connection failed.')
        return redirect(url_for('dashboard'))

@app.route('/add_grade', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        grade = request.form['grade']

        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)",
                       (student_id, course_id, grade))
        connection.commit()
        cursor.close()
        flash('Grade added successfully!')
        return redirect(url_for('view_grades'))
    
    return render_template('add_grade.html')

@app.route('/edit_grade/<int:grade_id>', methods=['GET', 'POST'])
def edit_grade(grade_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        grade = request.form['grade']
        
        cursor.execute("UPDATE grades SET student_id = %s, course_id = %s, grade = %s WHERE id = %s",
                       (student_id, course_id, grade, grade_id))
        connection.commit()
        cursor.close()
        flash('Grade updated successfully!')
        return redirect(url_for('view_grades'))
    
    cursor.execute("SELECT * FROM grades WHERE id = %s", (grade_id,))
    grade = cursor.fetchone()
    cursor.close()
    return render_template('edit_grade.html', grade=grade)

@app.route('/delete_grade/<int:id>', methods=['POST'])
def delete_grade(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM grades WHERE id = %s", (id,))
            connection.commit()
            flash('Grade deleted successfully!')
        except Exception as e:
            flash('Error deleting grade: ' + str(e))
        cursor.close()
    else:
        flash('Database connection failed.')
    return redirect(url_for('view_grades'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('home'))

# Home
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
