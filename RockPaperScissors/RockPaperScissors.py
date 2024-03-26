import random

def play():
    user = input("What's your choice?: 'r' for rock, 'p' for paper, 's' for scissors.\n") # Ask for user input
    computer = random.choice(['r','p','s']) # computer makes a random choice from the list
    
    if user == computer:  # If user made the same choice as the computer, then it's a tie
        return("It's a tie!")
      
    # r >s, s > p, p > r
    if is_win(user, computer):
        return "You won!"
        
    return 'You lost!' 

def is_win(player, opponent): # define a function for user winning choices
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())