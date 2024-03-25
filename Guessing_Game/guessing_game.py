import random
import sys


# Generate a random number to guess
rand_nr = random.randint(1, 9)


# Menu loop
def user():
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}")
    while True:
        user_choice = input("1. Play 2. Quit ")
        if user_choice == "1":
            print("Good, let's play!")
            break
        elif user_choice == "2":
            print(f"Good bye, {user_name}")
            sys.exit(0)
        else:
            print("Wrong choice!")
            continue
         
# Game loop
def game_loop():
    while True:
        user_choice = int(input("Guess the number: "))
        if user_choice == rand_nr:
            print("Congrats' you guessed the number :)")
            break
        elif user_choice >= 10:
            print("Your choice is too high")
            continue
        elif user_choice <= 1:
            print("Your choice is too low")
            continue
        else:
            print("Wrong number, try again: ")
            continue
        
# User's lives

        
# Call functions in main function
def main():
    user()
    game_loop()

# Call the function main to run the game    
if __name__ == "__main__":
    main()
        
        
