class Parent:
    def __init__(self):
        self.value="Inside Parent"
    
    def show(self):   #parent show method
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()  #call parent constructor
        self.value="Inside Child"

    def show(self):   #child show method
        print(self.value)

obj1=Parent()
obj2=Child()

obj1.show()
obj2.show()

 