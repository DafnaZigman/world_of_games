import random


def generate_sequence(difficulty):
    # Generate a list of random numbers between 1 and 101
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence


def get_list_from_user(difficulty):
    # Prompt the user for a list of numbers
    user_input = input(f"Enter {difficulty} numbers separated by a space: ")
    # Split the input string into a list of numbers
    user_list = []
    for x in user_input.split():
        if x.isdigit():
            user_list.append(int(x))
        else:
            print("Invalid input, try again.")
            return get_list_from_user(difficulty)
    # Validate the user's input
    if len(user_list) != difficulty:
        print("Invalid input, try again.")
        return get_list_from_user(difficulty)
    return user_list




def is_list_equal(list1, list2):
    # Compare the two lists and return True if they are equal, False otherwise
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def play_one(difficulty):
    from games_files.scores.utils import screen_cleaner
    while True:
        # Generate the sequence of numbers
        sequence = generate_sequence(difficulty)
        # Print the sequence for 0.7 seconds
        print(sequence)
        screen_cleaner()  # Call the screen_cleaner function here
        # Prompt the user for the numbers he remembers
        user_list = get_list_from_user(difficulty)
        # Compare the user's list with the original sequence
        if is_list_equal(sequence, user_list):
            print("You win!")
        else:
            print("You lose!")
        # prompt user to play again
        play_again = input("Would you like to play again (y/n)? ")
        if play_again.lower() == "y":
            play_one(difficulty)
        elif play_again.lower() == "n":
            screen_cleaner()  # Call the screen_cleaner function here
            break
        else:
            print("Please enter a valid response (y/n).")
print('Thank you for playing! Bye bye!')

