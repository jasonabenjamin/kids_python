import random

# Pick a random number between 1 and 10
number_to_guess = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 10. Try to guess it!")

# Keep playing until right guess
while True:
    guess = input("Enter your guess: ")
    
    # Has to be a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number!")
        break  # Exit the loop
