import random

# All the words for game - you can add your own
words = ["apple", "banana", "cherry", "orange", "grape"]

# Pick a random word
word = random.choice(words)

# Scramble the letters
scrambled = list(word)
random.shuffle(scrambled)
scrambled_word = "".join(scrambled)

# Start the game
print("Welcome to the Word Scramble Game!")
print("Try to guess the word from these scrambled letters:")
print(scrambled_word)

# Keep going until right guess
while True:
    guess = input("Your guess: ")
    if guess.lower() == word.lower():
        print("Correct! Well done!")
        break  # Exit the loop
    else:
        print("Oops! Try again.")
