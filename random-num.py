import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("Too low, try again!")
        guess = int(input("Guess a number between 1 and 100: "))
    else:
        print("Too high, try again!")
        guess = int(input("Guess a number between 1 and 100: "))

print("Congratulations! You guessed the correct number.")