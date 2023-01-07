# About data type in python

# String
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
# print("Hello")

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
import random

a = "Hello"
# print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

# Strings are Arrays
# Like many other popular programming languages,
# strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
# print(a[0])

# Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
# print(b[2:4])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
# print(b[-5:-2])

# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
# print(len(a))

# String Methods
# Python has a set of built-in methods that you can use on strings.
# strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
# print(len(a))
# print(a.strip())
# print(len(a.strip()))

# lower() method returns the string in lower case:
a = "Hello, World!"
# print(a.lower())

# upper() method returns the string in upper case:
a = "Hello, World!"
# print(a.upper())

# replace() method replaces a string with another string:
a = "Hello, World!"
# print(a.replace("H", "J"))

# split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
# print(a.split(","))
# result = a.split(",")
# print(result[0])
# print(result[1])

# Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
# print("RAIN".lower() in txt)

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
# print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
# print(c)

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {} are:
# age = 36
# txt = "My name is John, and I am {} "
# print(txt.format(age))

# The format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# Other escape characters used in Python:
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# Booleans
# Booleans represent one of two values: True or False.
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 200
# if b < a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Evaluate a string and a number:
# print(bool())

# Evaluate two variables:
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))
# print(bool(""))
# print(bool({1, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}))
# print(bool([]))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# In fact, there are not many values that evaluates to False,
# except empty values, such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.


# Integers
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1  # int
y = 35656222554887711  # int
z = -3255522  # int
# print(type(x))

# Floats
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10  # float
y = 1.0  # float
z = -35.59  # float
# print(type(x))

# Complex
# Complex numbers are written with a "j" as the imaginary part:
a = -5 + 1j
b = 7 + 6j
# calculate the sum and substrac of two complex numbers
result1 = a + b
result2 = a - b

# print("The sum of two complex numbers is: ", result1)
# print("The substrac of two complex numbers is: ", result2)

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
# Convert from one type to another:
# print(int(1))  # x will be 1
# print(int(2.8))  # x will be 2
# print(int("3"))  # x will be 3
# print(float(1))  # x will be 1.0
# print(float(2.8))  # x will be 2.8
# print(float("3"))  # x will be 3.0
# print(float("4.2"))  # x will be 4.2
# print(complex(1))  # x will be 1j
# print(complex(2.8))  # x will be (2.8+0j) # x will be 3j


# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

# print(random.randrange(1, 10))

# Python Casting
# There may be times when you want to specify a type on to a variable.
# This can be done with casting. Python is an object-orientated language,
# and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:
# x = int(1)  # x will be 1
# y = int(2.8)  # y will be 2

# # print(x)
# # print(y)


# List
# A list is a collection which is ordered and changeable. Allows duplicate members.
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
for x in thislist:
    print(x)

# Access Items
# You access the list items by referring to the index number:
print(thislist[1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
# for x in thislist:
#     print(x)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List Length
# To determine how many items a list has, use the len() method:
print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange")
print(thislist)

# Remove Item
# There are several methods to remove items from a list:
# The remove() method removes the specified item:
# thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()


# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Create and print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])

# Change Values
# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
print(thisdict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# Tuple
# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# But there is a workaround. You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.
# Convert the tuple into a list to be able to change it:
x = list(thistuple)
# Change the second item:
x[1] = "kiwi"
# Convert the list back into a tuple:
thistuple = tuple(x)
print(thistuple)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# Iterate through the items and print the values:
for x in thistuple:
    print(x)

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
