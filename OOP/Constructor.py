#Methods in python that are automatically called when object of a class is created
#In python , the constructor method always named "__init__"
class MyClass:
    def __init__(self):# constructor without paramerter
        print(f"I am a Constructor")

p1=MyClass()

class MsgPrint:
    def __init__(self,msg):# constructor with paramerter
        print(msg)

p1=MsgPrint("I am a Constructor 2")

