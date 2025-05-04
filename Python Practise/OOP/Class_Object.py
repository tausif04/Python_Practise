#Creating a Dog class and its object
class MyClass:
    x = 5
    y = 10
    #A function/method of adding within my class
    #"self" represent the instance of the class.
    def addTwo(self,p,q):
        z=10
        print(self.x+self.y+z+p+q)

p1 = MyClass()#p1 is a object of the class 'MyClass'
p1.addTwo(10,20)