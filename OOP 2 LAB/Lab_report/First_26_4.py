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

    # Overriding the 'taste' attribute
    def describe(self):
        self.taste = "Extra Sweet"  # Overridden
        return f"{self.name} is now described as {self.taste} and is mostly available in {self.season}."

mango = Mango("Mango", "Sweet", "Summer")
print(mango.describe())
