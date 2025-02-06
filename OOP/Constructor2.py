#Changing class variable using constructor params
class MyClass:
    x=0
    y=0
    def __init__(self):
        self.x=120
        self.y=180
p1=MyClass()
print(f"X={p1.x}")
print(f"Y={p1.y}")