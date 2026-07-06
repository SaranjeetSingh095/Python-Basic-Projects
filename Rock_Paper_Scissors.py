"""
Rock-Paper-Scissors Game
A simple game where the user plays against the computer.

Game Rules:
- Rock (0) beats Scissors
- Scissors (1) beats Paper
- Paper (2) beats Rock
"""

from random import randint

# Define choices
CHOICES = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

REVERSE_CHOICES = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

def get_user_choice():
    """Get and validate user input."""
    while True:
        user_input = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        
        if user_input == 'quit':
            return None
        
        if user_input in CHOICES:
            return CHOICES[user_input]
        else:
            print("❌ Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, ai_choice):
    """
    Determine the winner of the game.
    Returns: "win", "lose", or "draw"
    """
    if user_choice == ai_choice:
        return "draw"
    
    # Define winning conditions
    winning_conditions = {
        0: 2,  # Rock beats Scissors
        1: 0,  # Paper beats Rock
        2: 1   # Scissors beats Paper
    }
    
    if winning_conditions[user_choice] == ai_choice:
        return "win"
    else:
        return "lose"

def display_result(user_choice, ai_choice, result):
    """Display the game result."""
    user_choice_name = REVERSE_CHOICES[user_choice]
    ai_choice_name = REVERSE_CHOICES[ai_choice]
    
    print(f"\n{'='*50}")
    print(f"Your choice:     {user_choice_name.upper()}")
    print(f"Opponent choice: {ai_choice_name.upper()}")
    print(f"{'='*50}")
    
    if result == "draw":
        print("🤝 It's a Draw!")
    elif result == "win":
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")
    print(f"{'='*50}\n")

def play_game():
    """Main game loop."""
    print("\n" + "="*50)
    print("🎮 Welcome to Rock-Paper-Scissors Game! 🎮")
    print("="*50)
    
    while True:
        # Get user choice
        user_choice = get_user_choice()
        
        if user_choice is None:
            print("\nThanks for playing! Goodbye! 👋")
            break
        
        # Get AI choice
        ai_choice = randint(0, 2)
        
        # Determine winner
        result = determine_winner(user_choice, ai_choice)
        
        # Display result
        display_result(user_choice, ai_choice, result)
        
        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    play_game()
