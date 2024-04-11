# Bools and None

# Booleans can be True or False

a = True
b = False
# False is ALWAYS 0
# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True

# Boolean methods

hi = "Hello World"

# We can use these to make decisions
# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.isupper()) # False
# print(hi.endswith("d")) # True
# print(hi.startswith("H")) # True

# What happens when you try to convert a string to a bool
# print(bool(hi)) # True
# print(bool()) # False --> Empty string inputted

# What happens when we convert a number to a bool?
# print(bool(0))  # False
# print(bool(-40))  # True --> Any number other than 0 is true, even negatives

# The value of None

# None is an object, it is essentially a placeholder
# None when converted to a bool is False
print(bool(False))

# None != False
x = None
print(x == False)
print(x is None)

print(type(x))

# None is best used over an empty string etc. It is less likely to cause problems down the line.
