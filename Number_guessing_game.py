import random

print(" WELCOME  TO  THE  NUMBER  GUESSING  GAME :) ")

number = random.randint(1,100)
max_attempts = 7

print("Guess a number between 1 and 100")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess number : "))

    if guess == number:
        print("Congratulations !!! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print(f" Sorry, you have reached at maximum attempts to guess the number . The number was {number}.")
