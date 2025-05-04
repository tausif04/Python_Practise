# When Parent and  Chid class both has Constructor:
class Father:
    a=10
    b=20
    def __init__(self):
        print(self.a+self.b)

class Son(Father):
    x=100
    y=100
    def __init__(self):
        super().__init__()
        print(self.x+self.y)

obj=Son()