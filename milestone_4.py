#%%
import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word] # Should update to include guessed letters
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))# The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives
        self.word_list = ['banana', 'grape', 'strawberry', 'raspberry', 'orange']
        self.list_of_guesses = [] # list of guesses already tried
    
    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if not len(guess) == 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)