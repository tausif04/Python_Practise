#Method Overriding occurs when a subclass provides a new implementation for a mnethiod that
#already defined in its superclass
class Father:
    def addTwo(self,num1,num2):
        return num1+num2

class Son(Father):
    def addTwo(self,num1,num2):   #Child can override parent method
        print(f"Adding {num1} and {num2} in Son") 
        return num1+num2+1

# Creating instances of Father and Son
father=Father()
son=Son()  
 
# Calling the addTwo method from Father and Son
print(father.addTwo(5,3))
print(son.addTwo(5,3))