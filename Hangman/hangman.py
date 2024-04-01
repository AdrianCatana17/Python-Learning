import random # import random so we can select a random word from the list
from words import words # import the list with words
from stages import HANGMANPICS # import hangman visuals
import string # import string so we can check if input is a letter in alphabet

def get_word(words):
    word =random.choice(words) # randomly chooses a word from the list
    while '-' in word or ' ' in word: # if the word contain '-' or ' ', keep choosing the word
        word = random.choice(words)
    return word.upper() # if the word is valid, return the word in upper case

def hangman():
    word = get_word(words) 
    word_letters = set(word) # keep track of what already been guessed in the word
    alphabet = set(string.ascii_uppercase) # import the alphabet in upper case
    used_letters = set() # define a set to keep track of used letters
    
    lives = 6 # choose how many tries we have
    
    while len(word_letters) > 0 and lives > 0: # game loop 
        print(f"You have, {lives} lives left and you have used this letters: {used_letters}")
        
        word_list = [letter if letter in used_letters else "_" for letter in word] # if letter is in word, show the letter, else show "_"
        print(HANGMANPICS[lives]) # print hangman 
        print(f"Current word: {word_list}")
        
        user_letter = input("Guess a letter: ").upper() # ask the user for input
        if user_letter in alphabet - used_letters: # if the user input is a letter in alphabet and not in used letters add letter to used letter 
            used_letters.add(user_letter)
            print("")
            if user_letter in word_letters: # if the user input is in the secret word, we show the correct letter
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # if the user input is not in the secret word, then we lose a life 
                print(f"\nYour letter, {user_letter}, is not in the word")
        elif user_letter in used_letters: # if the user inputs the same letter twice, ask the user for a different input
            print("You have already guessed the letter, Guess another letter.")
        else: # if the user inputs something that is not a letter, tell the user he inputs a wrong character
            print(("\nThat is not a valid letter"))
    if lives == 0: # if we run out of lives, we lose
        print(HANGMANPICS[lives])
        print(f"You died. The words was {word}")
    else: # else, we won
        print("Congrats, you won!")
            





if __name__ == "__main__":
    hangman()