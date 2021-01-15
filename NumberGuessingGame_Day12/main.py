import random, art, sys

print(art.logo)
print("Welcome to the Number Guessing Game")

print("I'm thinking of a number between 1 and 100")
number = random.randint(1,100)
print(f"Hint: {number}")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == 'easy':
    no_of_attempts = 10
elif difficulty_level == 'hard':
    no_of_attempts = 5
else:
    print("Invalid input!")
    sys.exit()

while no_of_attempts > 0:
    print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low")

    elif guess > number:
        print("Too high.")
    
    else:
        print(f"You got it! The answer was {number}.")
        break

    if no_of_attempts == 1:
        print("You've run out of guesses, you lose.")
        break
    
    print("Guess again.")
    no_of_attempts -= 1
    continue


