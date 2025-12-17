import random

# Kid-friendly word list
words = ["cat", "dog", "sun", "moon", "tree", "fish", "star", "ball", "book", "duck"]

# Pick a random word
word = random.choice(words)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()   # Letters the player has guessed

# Number of tries
tries = 6

print("Welcome to Hangman!")
print("The word has " + str(len(word)) + " letters.")

# Game loop
while tries > 0 and word_letters != guessed_letters:
    # Show the word with guessed letters and underscores
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: " + " ".join(display_word))
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    if guess in word_letters:
        guessed_letters.add(guess)
        print("Good guess!")
    else:
        tries -= 1
        print("Oops! Wrong guess. Tries left: " + str(tries))

# End of game
if word_letters == guessed_letters:
    print("Congratulations! You guessed the word: " + word)
else:
    print("Game over! The word was: " + word)
