# Remade calculator program
from math_operators import add, subtract, divide, multiply, modulo
# Catch user inputs
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
# Execute every operation on inputted numbers
add_result = add(first_num, second_num)
sub_result = subtract(first_num, second_num)
div_result = divide(first_num, second_num)
mul_result = multiply(first_num, second_num)
mod_result = modulo(first_num, second_num)
# Print results
print(f"{first_num} + {second_num} = {add_result}")
print(f"{first_num} - {second_num} = {sub_result}")
print(f"{first_num} / {second_num} = {div_result}")
print(f"{first_num} * {second_num} = {mul_result}")
print(f"{first_num} % {second_num} = {mod_result}")
