#Constructor at Inheritance situation
#When parent class has constructor but child class has not
class Father:
    x=10
    y=110
    def __init__(self):
        print(self.x+self.y)

class Son(Father):
    x= 10
    print(x)

obj=Son()
print("------------")
#When parent class has constructor but child class has not
class Father:
    z=80
    x=20
class Son(Father):
    def __init__(self):
        print(self.z+self.x)

obj=Son()

print("------------")
#When parent class & child class both has constructor
class Father:
    x=10
    y=110
    def __init__(self):
        print(self.x+self.y)

class Son(Father):
    a=10
    b=20
    def __init__(self):
        super().__init__()
        #print(self.x+self.y)
        print(self.a+self.b)
obj=Son()