# About control statement in python

# if statement
import math
from math import pi

a = 10
if a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is zero")

print("------------ end of if statement ------------")

# while statement
i = 0
while i < 10:
    print(i)
    i += 1

print("------------ end of while statement ------------")

# switch statement
# switch statement is not available in python

# do while statement
# do while statement is not available in python

# for statement
for i in range(10):
    print(i)

print("------------ end of for statement ------------")

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

print("------------ end of break statement ------------")

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

print("------------ end of continue statement ------------")

# pass statement
for i in range(10):
    if i == 5:
        pass
    print(i)
# pass statement is used to avoid syntax error

print("------------ end of pass statement ------------")

# try statement
try:
    print(1 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError")

print("------------ end of try statement ------------")

# with statement
# with open("about_oop.py") as f:
#     for line in f:
#         print(line, end="")
# # with statement is used to avoid closing file manually

# print("------------ end of with statement ------------")

# assert statement
assert 1 == 1
# assert statement is used to check if the condition is true

print("------------ end of assert statement ------------")

# lambda statement


def f(x): return x * x


print(f(2))

print("------------ end of lambda statement ------------")

# yield statement


def f():
    for i in range(10):
        yield i


for i in f():
    print(i)

print("------------ end of yield statement ------------")

# del statement
a = [1, 2, 3]
del a[0]
print(a)
# del statement is used to delete an object

print("------------ end of del statement ------------")

# global statement
a = 10


def f():
    global a
    a = 20


f()
# print(a)

print("------------ end of global statement ------------")

# nonlocal statement
a = 10


def f():
    a = 20

    def g():
        nonlocal a
        a = 30

    g()
    print(a)


# f()

print("------------ end of nonlocal statement ------------")

# return statement


def f():
    return 1


print(f())
# return statement is used to return a value

print("------------ end of return statement ------------")

# import statement

print(math.pi)

print("------------ end of import statement ------------")

# from statement

print(pi)

print("------------ end of from statement ------------")

# class statement


class A:
    name = "A"


a = A()
print(a)
print(a.name)

print("------------ end of class statement ------------")
