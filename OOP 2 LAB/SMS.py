class Person:
    total_people = 0 

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
        Person.total_people += 1

    @classmethod
    def with_default_age(cls, name):
        """Alternate constructor with default age"""
        return cls(name=name, age=18)

    @classmethod
    def no_details(cls):
        """Alternate constructor with default details"""
        return cls()

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name="Unknown", age=0):
        super().__init__(name, age)
        self.enrolled_courses = []

    def add_course(self, course_name, instructor):
        """Add a course if it is not already enrolled."""
        if (course_name, instructor) not in self.enrolled_courses:
            self.enrolled_courses.append((course_name, instructor))

    def display(self):
        courses = ", ".join([f"{course} (Instructor: {instructor})" for course, instructor in self.enrolled_courses])
        return f"{super().display()}, Enrolled Courses: [{courses}]"

class Teacher(Person):
    def __init__(self, name="Unknown", age=0):
        super().__init__(name, age)
        self.teaching_schedule = []

    def assign_subject(self, subject, room_number):
        """Assign a subject if it is not already in the teaching schedule."""
        if (subject, room_number) not in self.teaching_schedule:
            self.teaching_schedule.append((subject, room_number))

    def display(self):
        schedule = ", ".join([f"{subject} (Room: {room})" for subject, room in self.teaching_schedule])
        return f"{super().display()}, Teaching Schedule: [{schedule}]"


if __name__ == "__main__":

    student1 = Student("Alice", 20)
    student2 = Student.with_default_age("Bob")
    student3 = Student.no_details()

    student1.add_course("Math", "Dr. Smith")
    student1.add_course("Physics", "Dr. Johnson")
    student2.add_course("Biology", "Dr. Brown")


    teacher1 = Teacher("Mr. Green", 35)
    teacher2 = Teacher.with_default_age("Ms. White")

    teacher1.assign_subject("Chemistry", "Room 101")
    teacher1.assign_subject("Physics", "Room 202")
    teacher2.assign_subject("English", "Room 103")

    print("-- Students --")
    print(student1.display())
    print(student2.display())
    print(student3.display())

    print("\n-- Teachers --")
    print(teacher1.display())
    print(teacher2.display())

    print(f"\nTotal People Registered: {Person.total_people}")
