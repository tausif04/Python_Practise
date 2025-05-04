class Fruits:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def describe(self):
        return f"{self.name} tastes {self.taste}."

class Mango(Fruits):
    def __init__(self, name, taste, season):
        super().__init__(name, taste)
        self.season = season

    def describe(self):
        return f"{self.name} tastes {self.taste} and is mostly available in {self.season}."

class Apple(Fruits):
    def __init__(self, name, taste, color):
        super().__init__(name, taste)
        self.color = color

class Orange(Fruits):
    def __init__(self, name, taste, is_seedless):
        super().__init__(name, taste)
        self.is_seedless = is_seedless

class Grapes(Fruits):
    def __init__(self, name, taste, variety):
        super().__init__(name, taste)
        self.variety = variety


mango = Mango("Mango", "Sweet", "Summer")
apple = Apple("Apple", "Sweet and Tangy", "Red")
orange = Orange("Orange", "Citrusy", True)
grapes = Grapes("Grapes", "Sweet", "Seedless")

print(mango.describe())
print(apple.describe())
print(f"{orange.name} tastes {orange.taste} and it is {'seedless' if orange.is_seedless else 'not seedless'}.")
print(f"{grapes.name} tastes {grapes.taste} and comes in {grapes.variety} variety.")
