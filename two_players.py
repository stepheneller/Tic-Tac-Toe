from game_parts import spaces, board
from game_checks import check_winner, check_spaces


def two_player(first_player, second_player):
    game_spaces = spaces
    game_board = board

    print("Okay, ready to play?")

    winner = False
    winner_name = None
    spaces_available = True
    turn = first_player
    spaces_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while not winner and spaces_available:

        if turn == first_player:
            print(f"It's {first_player}'s turn.")
            print(game_board)
            choice = int(input('Choose a spot on the board: Input a number\n'))
            if choice in spaces_list:
                game_spaces.update({choice: 'X'})
                game_board = f" {game_spaces[1]} | {game_spaces[2]} | {game_spaces[3]} \n" \
                             f"----------\n" \
                             f" {game_spaces[4]} | {game_spaces[5]} | {game_spaces[6]} \n" \
                             f"----------\n" \
                             f" {game_spaces[7]} | {game_spaces[8]} | {game_spaces[9]} \n"
                spaces_list.remove(choice)
                winner = check_winner(game_spaces)
                if winner:
                    winner_name = first_player
                spaces_available = check_spaces(spaces_list)
                turn = second_player
            else:
                print("Please input an available number...")

        elif turn == second_player:
            print(f"It's {second_player}'s turn.")
            print(game_board)
            choice = int(input('Choose a spot on the board: Input a number\n'))
            if choice in spaces_list:
                game_spaces.update({choice: 'O'})
                game_board = f" {game_spaces[1]} | {game_spaces[2]} | {game_spaces[3]} \n" \
                             f"----------\n" \
                             f" {game_spaces[4]} | {game_spaces[5]} | {game_spaces[6]} \n" \
                             f"----------\n" \
                             f" {game_spaces[7]} | {game_spaces[8]} | {game_spaces[9]} \n"
                spaces_list.remove(choice)
                winner = check_winner(game_spaces)
                if winner:
                    winner_name = second_player
                spaces_available = check_spaces(spaces_list)
                turn = first_player
            else:
                print("Please input an available number...")

    if not winner and not spaces_available:
        print(game_board)
        print("Oh no, looks like it ended in a draw!")

    elif winner:
        print(game_board)
        print(f"{winner_name} won! Congratulations!")
