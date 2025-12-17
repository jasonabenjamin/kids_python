import random

# Here is the list of words to pick from
words = ["cat", "dog", "sun", "moon", "tree", "fish", "star", "ball", "book", "duck"]

# Pick a random word
word = random.choice(words)

# Word letters as a list
word_letters = list(word)  # ['c','a','t']
guessed_letters = []       # List to track letters guessed by the player

# Number of tries
tries = 6

print("Welcome to Hangman!")
print("The word has " + str(len(word)) + " letters.")

# Game loop
while tries > 0:
    # Show the word with guessed letters and blanks
    display_word = []
    for letter in word_letters:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")
    print("Word: " + " ".join(display_word))
    
    # Check if all the word is guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word: " + word)
        break

    # Get the player's guess
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word_letters:
        print("Good guess!")
    else:
        tries -= 1
        print("Oops! Wrong guess. Tries left: " + str(tries))

# If the player ran out of tries
if tries == 0:
    print("Game over! The word was: " + word)
