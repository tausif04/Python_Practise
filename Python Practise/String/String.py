#Strings in Python are sequences of characters enclosed within single ( ' ' ), double ( " " ),or triple quotes ( ''' ''' or """ """ ).
#They are immutable , once created cannot be change
string1='Tausif Bin Mozid'
print("String 1: ",string1)

string2="Tausif Bin Mozid"
print("string-2:",string2)

string3='''Tausif Bin Mozid'''
print("String 3: ",string3)

string4="""Tauisf Bin Mozid"""
print("Sring 4: ",string4)

single_quote_str = 'Hello, World!'
print(single_quote_str)
# Output: Hello, World! Using single quotes inside the string

quote_in_str = 'He said, "Hello, World!"'
print(quote_in_str)
# Output: He said, "Hello, World!" - no need to escape since the inner quotes are double quotes.

# Using single quotes inside the string with escaping
escaped_quote_in_str = 'He said, \'Hello, World!\''
print(escaped_quote_in_str)
# Output: He said, 'Hello, World!' - escaped using a Double Quotes ( " " ) Triple Single Quotes ( ''' ''' )backslash (\)

triple_single_quote_str = '''This is a string
that spans multiple lines.
It can contain both "double quotes" and 'single quotes' without escaping.'''
print(triple_single_quote_str)


triple_double_quote_str = """This is another string
that spans multiple lines.
It also can contain both "double quotes" and 'single quotes' without escaping."""
print(triple_double_quote_str)