# ==========================================
# DOMAIN: Education (Digital Student Portal)
# ==========================================

class Course:
    """Represents a course offered in the portal."""

    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def get_course_info(self):
        return f"{self.course_code}: {self.course_name}"


class Student:
    """Represents a student in the system (Task 1: OOP Basics)."""

    # Class attribute to keep track of total active students
    total_students = 0

    def __init__(self, student_id, name, age):
        self.student_id = student_id  # Unique ID
        self.name = name  # Student Name
        self.age = age  # Student Age
        self.enrolled_courses = []  # List to hold Course objects

        # Increment total students whenever a new object is created
        Student.total_students += 1

    # Task 3: Instance Method (operates on specific object data)
    def enroll_course(self, course, grade):
        """Enroll student in a course using a Tuple (course, grade) for extra marks."""
        enrollment_record = (course, grade)
        self.enrolled_courses.append(enrollment_record)
        print(f"Successfully enrolled {self.name} in {course.get_course_info()} with Grade: {grade}")

    # Task 1 & 3: Instance Method to display student details
    def display_info(self):
        print(f"\n--- Student Record ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Enrolled Courses & Grades:")
        if not self.enrolled_courses:
            print("  No courses enrolled yet.")
        else:
            for course, grade in self.enrolled_courses:
                print(f"  - {course.get_course_info()} | Grade: {grade}")

    # Task 3: Class Method (operates on class-level data/attributes)
    @classmethod
    def get_total_students_count(cls):
        return f"Total Registered Students in System: {cls.total_students}"


# ==========================================
# Task 2: Python Data Structures & Functions
# ==========================================

# Using a Dictionary to store students with their unique ID as the key
student_database = {}


def add_student(student_id, name, age):
    """Function to add a new student record to the dictionary."""
    if student_id in student_database:
        print(f"Error: Student with ID {student_id} already exists!")
    else:
        new_student = Student(student_id, name, age)
        student_database[student_id] = new_student
        print(f"Student {name} added successfully!")


def display_all_students():
    """Function to loop through the dictionary and display all records."""
    if not student_database:
        print("No student records found.")
        return

    print("\n========================================")
    print("      COMPLETE STUDENT DIRECTORY        ")
    print("========================================")
    for student_id, student_obj in student_database.items():
        student_obj.display_info()
    print("========================================")


# ==========================================
# Example Usage / Sample Program Execution
# ==========================================
if __name__ == "__main__":
    print("--- 1. Creating Students Using Functions ---")
    add_student("S001", "Alice Kamara", 20)
    add_student("S002", "Mohamed Sesay", 22)

    print("\n--- 2. Creating Course Objects ---")
    course1 = Course("PROG211", "Object-Oriented Programming 1")
    course2 = Course("DBAS101", "Database Systems")

    print("\n--- 3. Using Instance Methods & Tuples (Extra Marks) ---")
    # Accessing student from dictionary and enrolling them in courses
    student_database["S001"].enroll_course(course1, "A")
    student_database["S001"].enroll_course(course2, "B+")

    student_database["S002"].enroll_course(course1, "A-")

    print("\n--- 4. Displaying All Records (Task 2 Loop) ---")
    display_all_students()

    print("\n--- 5. Using Class Method ---")
    print(Student.get_total_students_count())