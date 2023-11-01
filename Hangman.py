'''A simple game of hangman for the command line. Pulls from 58109 available words!'''
#%%
import random
import time

class Hangman():
    '''
    A class representing a game of Hangman.
    '''

    def __init__(self, word_list, num_lives):
        """
        Initialise a new game of Hangman.
        
        Parameters:
            word_list (list): A list of words for the game to choose from.
            num_lives (int): The number of lives the player starts with.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word] # Should update to include guessed letters
        self.num_unique_letters_remaining = len(set(self.word).difference(set(self.word_guessed)))# The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives
        self.word_list = ['banana', 'grape', 'strawberry', 'raspberry', 'orange']
        self.list_of_guesses = [] # list of guesses already tried
    
    def check_guess(self, guess):
        """
        Check the player's guess and update the game state accordingly.
        
        Parameters:
            guess (str): The letter guessed by the player.
        """
        guess = str.lower(guess)
        if guess in self.word:
            time.sleep(0.5)
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = letter
            self.num_unique_letters_remaining -= 1
        else:
            self.num_lives -= 1
            time.sleep(0.5)
            print(f"Sorry, {guess} is not in the word. Try again.")
            time.sleep(0.5)
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        """
        Prompt the player for a letter guess and validate the input.
        """

        guess = input('Enter a single letter: ')
        if not len(guess) == 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            incorrect_guesses = set(self.list_of_guesses).difference(set(self.word))
            time.sleep(1)
            if incorrect_guesses:
                print('Your incorrect guesses so far: ', list(incorrect_guesses))

def play_game(word_list):
    """
    The main game loop.
    
    Parameters:
        word_list (list): A list of words for the game to choose from.
    """

    while True:
        try:
            num_lives = int(input('How many lives would you like? '))
        except ValueError:
            print('Invalid character: please enter a number!')
            continue
        else:
            break
        

    game = Hangman(word_list, num_lives)

    while True: 
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_unique_letters_remaining > 0:
            time.sleep(0.2)
            print('Word to guess: ', game.word_guessed)
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_unique_letters_remaining <= 0:
            print('Congratulations. You won the game!')
            break
#%%
def main():
    """
    The entry point for the script. Reads the word list and starts the game.
    """
    
    try:
        with open('wordlist.txt', 'r') as wordlist:
            words = wordlist.read()
            wordlist = words.split('\n')
        if not wordlist:
            print('The word list is empty. Exiting.')
            return
    except FileNotFoundError:
        print('File not found. Exiting.')
        return

#%%
    play_game(wordlist)

if __name__ == "__main__":
    main()