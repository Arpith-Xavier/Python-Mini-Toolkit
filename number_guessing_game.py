import random

number = random.randint(1, 100)
attempts = 0

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")
print("I'm thinking of a number from 1 to 100.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid whole number!")
        continue

    if guess < 1 or guess > 100:
        print("Choose a number between 1 and 100!")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(f"\n🎉 Correct! You guessed it in {attempts} attempts!")
        break
