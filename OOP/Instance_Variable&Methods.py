class Employee:
    def __init__(self,company_name,employee_count):
        self.company_name=company_name      #Instance Variable
        self.employee_count=employee_count  #Instance Variable

    def display_company_info(self):         #Instance Method
        #using 'self' to access variable inside the class
        print(f"Company Name : {self.company_name}\nTotal Employee : {self.employee_count}")


emp1=Employee("Google",2000)
emp1.display_company_info()
emp2=Employee("Amazon",3000)
emp2.display_company_info()
print(f"Company Name (From outside of the class): {emp1.company_name}\nTotal Employees (From outside of the class): {emp1.employee_count}")
