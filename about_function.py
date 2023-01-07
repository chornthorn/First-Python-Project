# About function in python

def about_function():
    print("Function is a block of code which only runs when it is called.")
    print("You can pass data, known as parameters, into a function.")
    print("A function can return data as a result.")
    print("In python a function is defined using the def keyword:")
    print("def my_function():")
    print("    print(\"Hello from a function\")")
    print("To call a function, use the function name followed by parenthesis:")
    print("my_function()")
    print("Information about function in python")


# Call function
# about_function()

# parameter


def my_function(fname: str):
    print(fname + " Refsnes")


# my_function("Hello")

# Default parameter value


def default_para_fun(country="Norway"):
    print("I am from " + country)


# default_para_fun("Sweden")
# default_para_fun("India")
# default_para_fun()

# Return values
def return_value_fun(x):
    return 5 * x


result = return_value_fun(10)
# print(result)

# Keyword arguments


def keyword_arguments_fun(child3, child2, child1):
    print("The youngest child is " + child3)


# keyword_arguments_fun(child1="Emil", child3="Thorn", child2="Tobias")

# Arbitrary arguments, *args
def arbitrary_arguments_fun(*kids):
    print("The youngest child is " + kids[2])


# arbitrary_arguments_fun("Emil", "Tobias", "Linus")

# Arbitrary keyword arguments, **kwargs
def arbitrary_keyword_arguments_fun(**kid):
    print("His last name is " + kid["city"])


# arbitrary_keyword_arguments_fun(
#     fname="Tobias", lname="Refsnes", age=36, city="Trondheim")

# Passing a list as an argument


def passing_list_as_argument_fun(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

# passing_list_as_argument_fun(fruits)
