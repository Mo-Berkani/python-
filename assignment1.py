import random

def get_player_choice():
    while True:
        player_choice = input("Please choose rock, paper, or scissors: ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice!")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "Player"
    else:
        return "Computer"

player_wins = 0
computer_wins = 0

print("Welcome to rock-paper-scissors! This game ends when a player reaches three wins!")

while True:
    print(f"Round {player_wins + computer_wins + 1}:")
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"The computer chose {computer_choice}!")

    winner = determine_winner(player_choice, computer_choice)
    if winner == "Player":
        player_wins += 1
    elif winner == "Computer":
        computer_wins += 1

    print(f"You {winner.lower()} this round! The current score is: Player - {player_wins} Computer - {computer_wins}.\n")

    if player_wins == 3:
        print("You won! Would you like to play again? (Yes/No)")
        play_again = input().lower()
        if play_again != "yes":
            break
        else:
            player_wins = 0
            computer_wins = 0
    elif computer_wins == 3:
        print("Computer wins! Would you like to play again? (Yes/No)")
        play_again = input().lower()
        if play_again != "yes":
            break
        else:
            player_wins = 0
            computer_wins = 0

print("Program Terminates")
