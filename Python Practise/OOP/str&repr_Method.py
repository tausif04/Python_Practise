import datetime
#using built in class
mydate=datetime.datetime.now()

print(f"__str__() string :{mydate.__str__()}")
print(f"str() string : {str(mydate)}")

print(f"__repe__() string :{mydate.__repr__()}")
print(f"repr() string :{repr(mydate)}")

print("---------------------------------------------------")
#Using new class
class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.sea_creature_name=sea_creature_name
        self.sea_creature_age=sea_creature_age
    
    def __str__(self):
        return f"The creature type is {self.sea_creature_name} and the age is {self.sea_creature_age}"
    def __repr__(self):
        return f"Ocean(\'{self.sea_creature_name}\',{self.sea_creature_age})"
c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))