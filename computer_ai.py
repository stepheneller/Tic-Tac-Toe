import random


def computer_choice(difficulty, game_dictionary, spaces_list, order):

    # Checks each of the rows to see if it can prevent or get a tic-tac-toe, otherwise it picks a random space
    if difficulty == 'medium':
        if game_dictionary[1] == game_dictionary[2] or game_dictionary[6] == game_dictionary[9] or game_dictionary[5] \
                == game_dictionary[7]:
            return 3
        elif game_dictionary[2] == game_dictionary[3] or game_dictionary[4] == game_dictionary[7] or game_dictionary[5]\
                == game_dictionary[9]:
            return 1
        elif game_dictionary[1] == game_dictionary[3] or game_dictionary[5] == game_dictionary[8]:
            return 2
        elif game_dictionary[4] == game_dictionary[5] or game_dictionary[3] == game_dictionary[9]:
            return 6
        elif game_dictionary[5] == game_dictionary[6] or game_dictionary[1] == game_dictionary[7]:
            return 4
        elif game_dictionary[4] == game_dictionary[6] or game_dictionary[2] == game_dictionary[8] or game_dictionary[1]\
                == game_dictionary[9] or game_dictionary[3] == game_dictionary[7]:
            return 5
        elif game_dictionary[7] == game_dictionary[8] or game_dictionary[3] == game_dictionary[6] or game_dictionary[1]\
                == game_dictionary[5]:
            return 9
        elif game_dictionary[8] == game_dictionary[9] or game_dictionary[1] == game_dictionary[4] or game_dictionary[5]\
                == game_dictionary[3]:
            return 7
        elif game_dictionary[7] == game_dictionary[9] or game_dictionary[5] == game_dictionary[2]:
            return 8
        else:
            return random.choice(spaces_list)

    elif difficulty == 'hard':

        # checks for tic-tac-toe and prevents it or completes it
        if game_dictionary[1] == game_dictionary[2] or game_dictionary[6] == game_dictionary[9] or game_dictionary[5] \
                == game_dictionary[7]:
            return 3
        elif game_dictionary[2] == game_dictionary[3] or game_dictionary[4] == game_dictionary[7] or game_dictionary[5]\
                == game_dictionary[9]:
            return 1
        elif game_dictionary[1] == game_dictionary[3] or game_dictionary[5] == game_dictionary[8]:
            return 2
        elif game_dictionary[4] == game_dictionary[5] or game_dictionary[3] == game_dictionary[9]:
            return 6
        elif game_dictionary[5] == game_dictionary[6] or game_dictionary[1] == game_dictionary[7]:
            return 4
        elif game_dictionary[4] == game_dictionary[6] or game_dictionary[2] == game_dictionary[8] or game_dictionary[1]\
                == game_dictionary[9] or game_dictionary[3] == game_dictionary[7]:
            return 5
        elif game_dictionary[7] == game_dictionary[8] or game_dictionary[3] == game_dictionary[6] or game_dictionary[1]\
                == game_dictionary[5]:
            return 9
        elif game_dictionary[8] == game_dictionary[9] or game_dictionary[1] == game_dictionary[4] or game_dictionary[5]\
                == game_dictionary[3]:
            return 7
        elif game_dictionary[7] == game_dictionary[9] or game_dictionary[5] == game_dictionary[2]:
            return 8

        # depending on turn order, will initiate tactics to win the game or draw
        elif order == 'first':
            return 2
        elif game_dictionary[4] == 'O' and game_dictionary[5] == 'O':
            return 3
        elif game_dictionary[1] == 'O' or game_dictionary[3] == 'O':
            return 5
        elif game_dictionary[4] == 'O' or game_dictionary[7] == 'O' or game_dictionary[8] == 'O':
            return 1
        elif game_dictionary[6] == 'O' or game_dictionary[9] == 'O':
            return 3
        elif game_dictionary[5] == 'O':
            return 6

        # programming for going second
        elif game_dictionary[1] == 'X' or game_dictionary[3] == 'X' or game_dictionary[7] == 'X' or game_dictionary[9]\
                == 'X':
            return 5
        elif game_dictionary[2] == 'X':
            return 8
        elif game_dictionary[8] == 'X':
            return 2
        elif game_dictionary[4] == 'X':
            return 6
        elif game_dictionary[6] == 'X':
            return 4
        elif game_dictionary[5] == 'X':
            return 9
        elif game_dictionary[1] == game_dictionary[9] or game_dictionary[3] == game_dictionary[7]:
            return 2
        else:
            return random.choice(spaces_list)

    # For easy difficulty or another unknown entry, the computer will just select a random space available
    else:
        return random.choice(spaces_list)
