def my_function(a,b,c=0):
    print("a=",a)
    print("b=", b)
    print("c=", c)
    n=(a+b+c)*2
    return n
x= my_function(1,2,3)#positional argument
print(x)
x= my_function(10,20,)
print(x)
x= my_function(15,25,35)
print(x)

y=my_function(b=3,a=2,c=4)#named argument
print(y)