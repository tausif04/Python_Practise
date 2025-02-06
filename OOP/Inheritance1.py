# Single Inheritance
class Father:
    def addTwo(self,a,b):
        return a+b

class Son1(Father):
    print("I am Son1 ")

son1=Son1()
print(son1.addTwo(6,7))

print("----------------")
#Multiple Inheritance
class Addition:
    def addTwo(self,a,b):
        return a+b

class Subtraction:
    def subtractTwo(self,a,b):
        return a-b

class Calculation(Addition,Subtraction):
    pass

cal1=Calculation()
print(cal1.addTwo(8,9))
print(cal1.subtractTwo(9,8))

print("----------------")
#Multilevel Inherritance
class Father:
    def addTwo(self,num1,num2):
        return num1+num2
class Son(Father):
    pass
class GrandSon(Son):
    pass
grandson=GrandSon()
print(grandson.addTwo(5,3))