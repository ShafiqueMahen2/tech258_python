# Functions

# DRY - Don't Repeat Yourself

# Function with no arguments:

def print_something(name):
    print("Hello, my name is " + name)


print_something("Shafo")

# Function with args:

# def addition(num1, num2):
#     return num1 + num2
#
# print(addition(5,6))
# print(addition(10,15))

# Default arguments

# def addition(int1=2, int2=2):
#     return int1 + int2
#
#
# print(addition())
# print(addition(4,4))

# Multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    print("------------------")

multi_args(1, 2, 4, 6, 7)
multi_args(16, 24, 43)

# Type Hints
def division(denom: int, num: int) -> float:
    return denom / num

print(division(5, 5))