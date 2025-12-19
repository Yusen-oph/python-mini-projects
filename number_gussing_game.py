import random
number = random.randint(1,100)
attempts = 0
print("Welcome to the Number Guessing Game! You got as many attempts as you want to guess the number between 1 to 100.")
print("Your goal is to guess the number in as few attempts as possible!")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too small! Try again.")
    elif guess > number:
        print("Too big! Try again.")
    else:
        print("Congratulations! You've gussed the number", number, "in", attempts, "attempts.")
        break