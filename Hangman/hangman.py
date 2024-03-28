import random
from words import words
from stages import HANGMANPICS
import sys

def get_word(words):
    word =random.choice(words) # randomly chooses a word from the list
    while '-' in word or ' ' in word: # if the word contain '-' or ' ', keep choosing the word
        word = random.choice(words)
    return word.upper() # if the word is valid, return the word in upper case

def menu():
    username = input("Hi, what's your name? \n") # ask user for his name
    print(f"Hello, {username}, let's play Hangman!")
    global choice 
    choice = input("1. Play \n2. Quit \n") # global variable choosing if we play or quit
    while True:
        if choice == "1":
            continue
        elif choice == "2":
            sys.exit()
        else:
            print("Wrong choice. Try again!")
            continue
    
def main():
    missedLetters = []
    correctLetters = []
    word = "_" * len(get_word(words)) # change the word letters with "_"
    while True: # main game loop
        pass
            
    

def draw_hangman():
    pass

if __name__ == "__main__":
    main()