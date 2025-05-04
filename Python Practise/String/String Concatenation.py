#String concatenation is the process of combining two or more strings into one

string1="Tausif"
string2="Bin"
string3="Mozid"
#using "+" Operator
combined=string1+" "+string2+" "+string3
print(combined)

#using join() method
combined=" ".join([string1,string2,string3])
print(combined)

#Using formatted string literals (f-strings)
combined=f"{string1} {string2} {string3}"
print(combined)

#Using the format() method:
string1 = "Hello"
string2 = "World"
combined = "{},{}!".format(string1, string2)
print(combined)

#Using % formatting:
string1 = "Hello"
string2 = "World"
combined = "%s, %s!" % (string1, string2)
print(combined)