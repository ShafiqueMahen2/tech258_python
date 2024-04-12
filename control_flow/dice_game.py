import random
import time

# Welcome Message
while True:
    ready = input("Hello and welcome to the dice game! Enter 'R' when ready!: ")
    if ready.upper() == "R":
        break
    else:
        print("Still waiting to see if you're ready... ")

# Get the user's name
name = input("Please enter your name! ")
name = name.capitalize()

# Session score (for multiple games played in a session)
user_session_wins = 0
cpu_session_wins = 0

# Game logic
while True:
    user_score = 0
    cpu_score = 0

    while user_score < 30 and cpu_score < 30:
        user_roll = random.randint(1, 6)
        cpu_roll = random.randint(1, 6)

        print(f"{name} rolled {user_roll}")
        print(f"CPU rolled {cpu_roll}")


        if user_roll > cpu_roll:
            print("Congrats! You beat the CPU! You earned 3 points")
            user_score += 3
        elif cpu_roll > user_roll:
            print("Unlucky! You lost to the CPU! The CPU has earned 3 points")
            cpu_score += 3
        else:
            print("It's a tie! You both earn 1 point")
            user_score += 1
            cpu_score += 1

        print(f"Current standings: {name} {user_score} - {cpu_score} CPU")
        print("--------------------------")
        time.sleep(3)

    if user_score >= 30 > cpu_score:
        print(f"Congrats on beating the CPU! Here's the final results: {name} {user_score} - {cpu_score} CPU")
        user_session_wins += 1
    elif cpu_score >= 30 > user_score:
        print(f"The CPU won, better luck next time! Here's the final results: {name} {user_score} - {cpu_score} CPU")
        cpu_session_wins += 1
    else:
        print("It's a tie! There are no winners in this game!")

    print(f"Current session standings: {name} {user_session_wins} - {cpu_session_wins} CPU")
    play_again = input("Do you want to play again? (Enter 'Yes' to continue): ")
    if play_again.lower() != "yes":
        break

print(f"Thank you for playing! Here are the final Session standings: {name} {user_session_wins} - {cpu_session_wins} CPU")
print("Goodbye!")
