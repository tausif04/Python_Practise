class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
        Student.total_students += 1  

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0  

    def is_passing(self, passing_grade):
        if self.grades:  
            if self.average_grade() >= passing_grade:
                print(f"{self.name}, age {self.age}, is passing with an average grade above {passing_grade}.")
            else:
                print(f"{self.name}, age {self.age}, is not passing. Average grade is below {passing_grade}.")
        else:
            print(f"{self.name}, age {self.age}, has no grades yet.")


student1 = Student("Tausif", 22)
student1.add_grade(100)
student1.add_grade(70)
student1.add_grade(60)
student1.add_grade(62)


print(f"Average Grade: {student1.average_grade():.2f}")
student1.is_passing(40)
