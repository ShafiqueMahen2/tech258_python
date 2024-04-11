# Control Flow Tasks

## Task 1

This task is about creating a program that checks if a user can watch a movie based on the users age. This is done through a if/elif block. By comparing the stored data in `film_rating` variable to the rating in the if/elif condition. The program will be able to determine and print the suitability of the movie based on the rating.

The code itself goes through each classification being Universal, PG, 12, 12A, 15, 18 and if the `film_rating` variable doesn't match it will continue to the next elif. However, if a match is found the code prints the corresponding statement and terminates. If there is no match, the print statement in the else block is printed instead, prompting the user to store a correct classification in the `film_rating` variable.

## Task 2

### What are loops? What are the different types? And what can we do with them?
Loops in programming are control structures used to repeat a block of code multiple times. They enable us to automate repetitive tasks in an efficient manner. The two main types of loops are:

- For loop: Iterates over a sequence e.g. list/range for a specified number of times.
- While loop: Repeats a code block as long as the specified condition is True.

### What is a for loop? Show an example (use code block)
A for loop iterates over a sequence for a specified number of times, here's an example:#
```python
for i in range(5):
    print("Iteration:", i)
```

This example will print numbers from 0 to 4 as `range(5)` starts from 0 and goes up to (not including) 5.
### What is a While loop? Why use one instead of a for loop? Show an example (use code block)
A while loop repeats a code block so long as a specified condition is true. It's useful for when the number of iterations is unknown beforehand or when looping based on a condition. Here's an example:
```python
num = 0
while num < 5:
    print("Current number", num)
num += 1
```
This code will print numbers from 0 to 4, incrementing the `num` variable in each iteration until it reaches 5, ending the loop as the condition is no longer met (5 isn't < 5 anymore).

### Are there any dangers to using loops? Any best practices to consider?
Loops can also lead to performance issues if used incorrectly, especially with larger datasets. If loops aren't crafted properly, they may lead to a infinite loop being created essentially freezing your program and perhaps PC. Some best practices to avoid this are:

- Avoid Nested Loops
- Optimise Loop Logic
- Consider Alternatives (libraries, etc)
