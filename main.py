# Play tic-tac-toe with a friend or against a computer by running the main.py!

# Rules for tic-tac-toe:
# The players will have the option of being Xs or Os
# The player who chooses X will always go first
# Players will alternate until one player gets three of their characters in a row, or spaces run out on the board
# Characters are in a row when they are 3 across, up, down, or diagonal

from two_players import two_player
from computers import computer_player


def start():
    print("Welcome!")
    name = str(input("What's your name?\n")).title()
    opponent = str(input('Do you want to play against a friend or a computer?: enter "friend" or "computer"\n')).lower()
    player_two = True

    if opponent == 'friend':
        friend = str(input("What's your friend's name?\n")).title()

    elif opponent == 'computer':
        player_two = False
        difficulty = str(input("What difficulty would you like the computer to be?: enter 'easy', 'medium', or 'hard'\n"
                               "")).lower()

    else:
        print("I'm sorry I didn't understand...")
        start()

    player_order = str(input(f"{name} would you like to go first or second? enter 'first' or 'second'\n")).lower()
    if player_order == 'first' and player_two:
        print(f"Okay, {name} will be Xs and {friend} will be Os.")
        two_player(name, friend)
    elif player_order == 'second' and player_two:
        print(f"Okay, {friend} will be Xs and {name} will be Os.")
        two_player(friend, name)
    elif player_order == 'first' and not player_two:
        print(f"Okay, you will be Xs and the computer will be Os.")
        computer_player(name, "Computer", name, difficulty)
    elif player_order == 'second' and not player_two:
        print(f"Okay, the computer will be Xs and you will be Os")
        computer_player("Computer", name, name, difficulty)


start()
