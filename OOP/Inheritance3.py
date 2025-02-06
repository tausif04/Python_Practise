# If Parent has static properties, child can access as it is like parent
class Father:
    a=10
    b=20
    @staticmethod
    def addTwo():
        print(Father.a+Father.b)

class Son(Father):
    pass

Son.addTwo()

Father.addTwo()

print(Father.a)
print(Father.b)

print("-----------X-------------")
#If Child has static properties, Parent can't access as it is like child

class Father:
    pass
class Son(Father):
    a = 10
    b = 20
    @staticmethod
    def addtwo():
        print(Son.a + Son.b)

Son.addtwo()

#Father.addtwo() #Parent can't access as it is like child

print(Son.a)
print(Son.b)

print("-----------X-------------")

# How child can access parents static and non-static properties
class Father:
    a = 10
    b = 20
    @staticmethod
    def addtwo():
        print(Father.a + Father.b)

    def addthree(self):
        print(self.a + self.b+10)


class Son(Father):
    def addnew(self):
        self.addthree()
        Father.addtwo()

obj=Son()
obj.addnew()