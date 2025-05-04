import json

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if student and course:
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid student ID or course code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if student and course and course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Ensure student is enrolled in the course before assigning a grade.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        student = self.students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        course = self.courses.get(course_code)
        if course:
            course.display_course_info()
        else:
            print("Course not found.")

    def save_data(self):
        data = {
            "students": {sid: {"name": s.name, "age": s.age, "address": s.address, "courses": s.courses, "grades": s.grades} for sid, s in self.students.items()},
            "courses": {code: {"course_name": c.course_name, "instructor": c.instructor, "students": [s.student_id for s in c.students]} for code, c in self.courses.items()}
        }
        with open("data.json", "w") as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                self.students = {sid: Student(d["name"], d["age"], d["address"], sid) for sid, d in data["students"].items()}
                for sid, student_data in data["students"].items():
                    self.students[sid].courses = student_data["courses"]
                    self.students[sid].grades = student_data["grades"]
                
                self.courses = {code: Course(d["course_name"], code, d["instructor"]) for code, d in data["courses"].items()}
                for code, course_data in data["courses"].items():
                    for sid in course_data["students"]:
                        if sid in self.students:
                            self.courses[code].add_student(self.students[sid])
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

    def run(self):
        while True:
            print("\n==== Student Management System ====")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("7. Save Data to File")
            print("8. Load Data from File")
            print("0. Exit")
            option = input("Select Option: ")

            if option == "1":
                self.add_student()
            elif option == "2":
                self.add_course()
            elif option == "3":
                self.enroll_student_in_course()
            elif option == "4":
                self.add_grade_for_student()
            elif option == "5":
                self.display_student_details()
            elif option == "6":
                self.display_course_details()
            elif option == "7":
                self.save_data()
            elif option == "8":
                self.load_data()
            elif option == "0":
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
