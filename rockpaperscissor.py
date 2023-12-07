import random

# Function to get user input
def get_user_choice():
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  while user_choice not in ["rock", "paper", "scissors"]:
    user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
  return user_choice

# Function to generate computer choice
def get_computer_choice():
  computer_choice = random.choice(["rock", "paper", "scissors"])
  return computer_choice

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
  win_conditions = {
    "rock": {"scissors": "crushes", "paper": "covers"},
    "paper": {"rock": "covers", "scissors": "cuts"},
    "scissors": {"paper": "cuts", "rock": "crushes"}
  }
  if user_choice == computer_choice:
    return "tie"
  elif computer_choice in win_conditions[user_choice]:
    return "lose", win_conditions[user_choice][computer_choice]
  else:
    return "win", win_conditions[computer_choice][user_choice]

# Initialize score variables
user_score = 0
computer_score = 0

# Game loop
while True:
  # Get user and computer choices
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()

  # Determine the winner
  result, message = determine_winner(user_choice, computer_choice)

  # Display results
  print(f"\nYou chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")
  if result == "win":
    print(f"You {result}! {message}")
    user_score += 1
  elif result == "lose":
    print(f"You {result}. {message}")
    computer_score += 1
  else:
    print("It's a tie!")

  # Display scores
  print(f"\nYour score: {user_score}")
  print(f"Computer score: {computer_score}")

  # Ask user to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    break

print("\nThanks for playing!")