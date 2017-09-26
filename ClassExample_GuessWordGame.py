WORD_LIST = ['biodun', 'bayo', 'ben', 'tomi', 'chidera', 'affiong', 'effiong', 'james']
import random

def pick_word(list_word):
    word  = random.choice(list_word)
   
    return word


def get_guess():
    
    guess = input('Guess a word:')
    if not guess == '':
        return guess
    else:
        print('Word cannot be empty')
    get_guess()


def evaluate_guess():
    
    word = pick_word(WORD_LIST)
    guess = get_guess()

    if guess == word:
        
        return True
        
    else:
        return False


def play_game():
   
    if evaluate_guess() == True:
        resp = input('Do you want to play again? y/n')
        if resp == 'y':
            play_game()
        else:
            print('Goodbye')
            exit()

    else:
        evaluate_guess()

##def play_game():
##  print('Hey, Welcome to my game')
##  game_count = 5
##  attempts = 0
##  max_attempt = 5
##
##  while game_count > 0:
##      game_count -= 1

        
play_game()
