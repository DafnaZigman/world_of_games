import random

from currency_converter import CurrencyConverter




def get_money_interval(difficulty):
    difficulty = int(difficulty)
    d = difficulty
    global t
    global result_convert
    t = random.randint(1, 100)
    a = CurrencyConverter()
    result_convert = int(a.convert(t, "USD", "ILS"))
    return (result_convert - (5 - d), result_convert + (5 - d))


def get_guess_from_user_2():
    while True:
        amount = input("Enter the amount in USD: ")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print("Please enter a valid value")
    while True:
        guess = input("Enter your guess in ILS: ")
        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Please enter a valid value")
    return guess


def play_three(difficulty):
    from games_files.scores.utils import screen_cleaner
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user_2()
    if interval[0] <= guess <= interval[1]:
        print("You won!")
    else:
        print("You lost :(")
    while True:
        play_again = input("Do you want to play again (yes/no)? ")
        if play_again in ["yes", "no"]:
            screen_cleaner()  # Call the screen_cleaner function here
            break
        else:
            print("Please enter a valid response (yes/no)")
    if play_again == "yes":
        play_three(difficulty)
    else:
        print("Goodbye! Thank you for playing.")



