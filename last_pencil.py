import string
import random


# ---------- constants -----------


player_1 = "User"
player_2 = "Bot"
pencil = "|"
err_str = {"not_a_numeric": "The number of pencils should be numeric",
           "not_positive": "The number of pencils should be positive",
           "wrong_name": f"Choose between {player_1} and {player_2}",
           "impossible_value": "Possible values: '1', '2' or '3'",
           "too_many_pencils": "Too many pencils were taken"}
bot_turn_values = {1: random.randint(1, 3),
                   2: 1,
                   3: 2,
                   0: 3}
winner_tmpl = string.Template("$name won!")


# ---------- init game ----------


def init_number_of_pencils():
    print("How many pencils would you like to use:")
    while True:
        try:
            n_pencils = input()
            if not n_pencils.isdigit():
                raise ValueError("not_a_numeric")
            n_pencils = int(n_pencils)
            if n_pencils == 0:
                raise ValueError("not_positive")
        except ValueError as err:
            print(err_str[str(err)])
            continue
        else:
            return n_pencils
        

def init_first_player():
    print(f"Who will be the first ({player_1}, {player_2})")
    while True:
        try:
            first = input()
            if first not in [player_1, player_2]:
                raise ValueError("wrong_name")
        except ValueError as err:
            print(err_str[str(err)])
            continue
        else:
            return first


def init_game():
    n_pencils = init_number_of_pencils()
    first = init_first_player()
    return [n_pencils, first]


# ---------- game turn ----------


def bot_turn(n_pencils):
    if n_pencils == 1:
        bot_input = 1
    else:
        remainder = n_pencils % 4
        bot_input = bot_turn_values[remainder]
    print(bot_input)
    return n_pencils - bot_input


def user_turn(n_pencils):
    while True:
        try:
            remove = input()
            if remove not in string.digits:
                raise ValueError("impossible_value")
            remove = int(remove)
            if not 1 <= remove <= 3:
                raise ValueError("impossible_value")
            if remove > n_pencils:
                raise ValueError("too_many_pencils")
        except ValueError as err:
            print(err_str[str(err)])
            continue
        else:
            return n_pencils - remove


def game_turn(n_pencils, active_player):
    if active_player == player_1:
        return user_turn(n_pencils)
    return bot_turn(n_pencils)


# ---------- main script ----------

def main():
    n_pencils, active_player = init_game()
    while n_pencils > 0:
        print(n_pencils * pencil)
        print(f"{active_player}'s turn:")
        n_pencils = game_turn(n_pencils, active_player)
        active_player = player_1 if active_player == player_2 else player_2
    print(winner_tmpl.substitute(name=active_player))


if __name__ == "__main__":
    main()