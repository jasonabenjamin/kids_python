import random

# Possible choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")
print("Type 'quit' to exit the game.")

while True:
    # What you pick
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    # What the computer picks
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")
    
    # Find the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
    
    print()  # Just blank line
