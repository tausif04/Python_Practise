"""String slicing in Python allows you to extract a portion of a string using a colon ( : ) syntax. The
basic form of slicing is string[start : stop : step] , where
                          start is the index where the slice starts (inclusive).
                         stop is the index where the slice ends (exclusive).
                         step determines the step size or the increment between each index."""

text = "Hello, World!"
print(text[0:5]) #Extracts a Substring from Index 0 to 4
print(text[7:])   #Extracts from Index 7 to the End
print(text[:5])   #Extracts from the Start to Index 4
print(text[::2])  #Extracts Every Second Character
print(text[::-1])  #Reverses the String
print(text[0::3])  #Extract every third character starting from index 0
print(text[3:8])   # Extract substring from index 3 to 8