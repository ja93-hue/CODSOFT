#simple application to play rock , paper , scissors game with the system using python. it prompts the user to choose an option.
#it displays the score and winner of the round and asks if the user is interested to play another round.
import random

def game(user_choice, system_choice, u_score, s_score):
    
    win_choices = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    
    if user_choice == system_choice:
        print(f"Both chose {user_choice}. It's a tie!")
    elif win_choices[user_choice] == system_choice:
        print(f"{user_choice} beats {system_choice}. You win this round!")
        u_score += 1
    else:
        print(f"{system_choice} beats {user_choice}. You lose this round!")
        s_score += 1

    return u_score, s_score

def main():
    u_score = 0
    s_score = 0
    options = ["rock", "paper", "scissors"]

    print("\nROCK PAPER SCISSORS GAME")

    new_game = True
    while new_game:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").strip().lower()
        while user_choice not in options:
            user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").strip().lower()
        
        system_choice = random.choice(options)
        print(f"\nYou chose {user_choice}. The system chose {system_choice}.")
        print("\nGAME BEGINNN!!!")
        
        u_score, s_score = game(user_choice, system_choice, u_score, s_score)

        print(f"\nCurrent Score -> You: {u_score} | System: {s_score}")

        new_game = input("\nHow about a new match? (yes/no): ").strip().lower() == "yes"

    print("\nFinal Score -> You: {u_score} | System: {s_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
