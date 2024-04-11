x = 0

while x < 10:
    if x > 4:
        break
    print(f"Value of x this iteration is: {x}")
    x+=1

# If we didn't increment x each iteration, the value of x would remain the same, creating a infinite loop.
