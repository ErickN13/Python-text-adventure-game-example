def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go left or right.")
    choice = input("Which way do you want to go? (left/right): ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        start_game()

def left_path():
    print("You walk down the left path and encounter a wild animal.")
    choice = input("Do you want to run or fight? (run/fight): ").lower()

    if choice == "run":
        print("You run away safely. You win!")
    elif choice == "fight":
        print("You fight bravely but the animal overpowers you. You lose.")
    else:
        print("Invalid choice. Please type 'run' or 'fight'.")
        left_path()

def right_path():
    print("You walk down the right path and find a treasure chest.")
    choice = input("Do you want to open it? (yes/no): ").lower()

    if choice == "yes":
        print("You open the chest and find a treasure. You win!")
    elif choice == "no":
        print("You leave the chest and walk away. You win!")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        right_path()

start_game()
