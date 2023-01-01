from games_files.memory_game import play_one
from games_files.guess_game import play_two
from games_files.currency_roulette_game import play_three


# print("Hello from live.py!")

def welcome():
    """Welcome to the game"""


name = ''

while True:
    name = input("Hello, Please type your name \n ").title()

    if not name.isalpha():
        print("Enter only letters")
        continue
    else:
        print(f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.\n")
        break


def load_game():
    """This function asks the user to enter a game and to choose a difficulty"""

    # Import the add_score function from the score module
    from games_files.scores.score import add_score



    while True:

        game_num = input(
            """Please choose a game to play:\n
             1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n
             2. Guess Game - guess a number and see if you chose like the computer\n
             3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n""")
        if game_num.isnumeric():
            game_num = int(game_num)

        if game_num not in range(1, 4):
            print("invalid input.Try Again Please")
            continue
        else:
            print(f"You chose game number  {game_num}:")
        break

    while True:

        difficulty = input("Please chose a game difficulty between 1 to 5: ")
        if difficulty.isnumeric():
            difficulty = int(difficulty)
            if difficulty in range(1, 6):
                print(f"You chose difficulty number : {difficulty}")

            else:
                print("invalid input.Try Again Please")

            if game_num == 1:
                play_one(difficulty)
                # Call the add_score function after the game has been played
                add_score(difficulty)
                break
            elif game_num == 2:
                play_two(difficulty)
                # Call the add_score function after the game has been played
                add_score(difficulty)
                break
            elif game_num == 3:
                play_three(difficulty)
                # Call the add_score function after the game has been played
                add_score(difficulty)
                break
