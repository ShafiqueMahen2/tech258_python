# Simple calculator functions
# import math_operators
# from math_operators import add, subtract, divide, multiply
from math_operators import *

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
# result = math_operators.add(first_num, second_num)
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")

# A module is a single file.

# A package is multiple modules bundled together into one.

# A library is a general term we can use (as a catch-all). Tends to be used for large packages.

