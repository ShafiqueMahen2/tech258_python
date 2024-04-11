# Task 3
x = 0

while x < 10:
    if x > 4:
        break
    print(f"Value of x this iteration is: {x}")
    x+=1

# If we didn't increment x each iteration, the value of x would remain the same, creating a infinite loop.

# Task 4
user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        print("Inputted value is invalid or too high, please try again!")

print(f"Your age is {age}")