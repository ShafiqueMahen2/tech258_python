# Mixed Lists

mixture = [1, 2, 3, "one", "two", "three"]
print(type(mixture))

name = input("Please enter your name: ")
age = input("Please enter your age: ")
dob = input("Please enter your DOB: ")
height_cm = input("Please enter your height, in cm: ")
user_details = [name, int(age), dob, float(height_cm)]
print(user_details)
print("Hi" + user_details[0])
print(user_details[1])
print(user_details[2])
print(user_details[3])