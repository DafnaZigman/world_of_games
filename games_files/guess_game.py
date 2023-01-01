import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess = input("Enter a number between 1 and {}: ".format(difficulty))
    guess = int(guess)
    return guess


def compare_results(secret_number, guess):
    if guess == secret_number:
        return "You won!"
    else:
        return "You lost. The correct number was {}.".format(secret_number)


def play_two(difficulty):
    from games_files.scores.utils import screen_cleaner
    while True:
        secret_number = generate_number(difficulty)
        guess = get_guess_from_user(difficulty)
        result = compare_results(secret_number, guess)
        print(result)  # Print the result message here

        play_again = input("Would you like to play again (y/n)? ")
        if play_again.lower() == "y":
            screen_cleaner()  # Call the screen_cleaner function here
            continue  # Continue the outer loop
        elif play_again.lower() == "n":
            break  # Break out of the outer loop
        else:
            print("Please enter a valid response (y/n).")

print('Thank you for playing! Bye bye!')



