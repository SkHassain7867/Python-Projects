import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

number = random.randint(1, 100)
attempts = 0

while True:

    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too Low! Try again.")

        elif guess > number:
            print("Too High! Try again.")

        else:
            print("\nCongratulations! 🎉")
            print("You guessed the correct number.")
            print("Number:", number)
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")