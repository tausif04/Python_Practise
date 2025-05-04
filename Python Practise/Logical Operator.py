#Logical Operator: Logical operators are used to combine conditional statements. The most common logical operators in Python are and , or , and not

"""The and operator returns True if both conditions are True . If either condition is False , the
result is False"""
age = 20
has_permission = True
if age >= 18 and has_permission:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")


"""The or operator returns True if at least one of the conditions is True . If both conditions are
False , the result is False ."""
age = 16
has_permission = True
if age >= 18 or has_permission:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")


"""The not operator inverts the result of the condition. If the condition is True , not makes it
False , and if the condition is False , not makes it True ."""
age = 16
if not age >= 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

#You can combine multiple logical operators to form more complex conditions
age=20
has_permission=False
is_vip=True

if(age>=18 and has_permission) or is_vip:
    print("You can enter the club")
else:
    print("You cannot enter the club")