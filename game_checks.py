def check_spaces(available_spaces):
    if len(available_spaces) > 0:
        return True
    else:
        return False


def check_winner(game_dictionary):
    if game_dictionary[1] == game_dictionary[2] == game_dictionary[3]:
        return True
    elif game_dictionary[4] == game_dictionary[5] == game_dictionary[6]:
        return True
    elif game_dictionary[7] == game_dictionary[8] == game_dictionary[9]:
        return True
    elif game_dictionary[1] == game_dictionary[4] == game_dictionary[7]:
        return True
    elif game_dictionary[2] == game_dictionary[5] == game_dictionary[8]:
        return True
    elif game_dictionary[7] == game_dictionary[8] == game_dictionary[9]:
        return True
    elif game_dictionary[1] == game_dictionary[5] == game_dictionary[9]:
        return True
    elif game_dictionary[3] == game_dictionary[5] == game_dictionary[7]:
        return True
    else:
        return False
