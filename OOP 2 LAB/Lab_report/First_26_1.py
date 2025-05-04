class Bird:
    def __init__(self, name, color, can_fly):
        self.name = name
        self.color = color
        self.can_fly = can_fly

    def sing(self):
        return f"{self.name} is singing beautifully."

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying high in the sky."
        return f"{self.name} cannot fly."

    def __str__(self):
        return f"Bird(Name: {self.name}, Color: {self.color}, Can Fly: {self.can_fly})"


bird1 = Bird("Parrot", "Green", True)
bird2 = Bird("Penguin", "Black and White", False)
bird3 = Bird("Sparrow", "Brown", True)
bird4 = Bird("Ostrich", "Gray", False)
bird5 = Bird("Peacock", "Colorful", True)


birds = [bird1, bird2, bird3, bird4, bird5]

for bird in birds:
    print(bird)
    print(bird.sing())
    print(bird.fly())
    print()
