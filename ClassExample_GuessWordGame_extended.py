
WORD_LIST = ['biodun', 'bayo', 'ben', 'tomi', 'chidera', 'affiong', 'effiong', 'james']
max_attempts = 5


import random

def pick_word(list_word):
    word  = random.choice(list_word)
    print('The correct word is,', word)
    return word


def get_guess():
    
    guess = input('Guess a word:')
    if not guess == '':
        return guess
    else:
        print('Word cannot be empty')
    get_guess()


def evaluate_guess(attempts_left):
    word = pick_word(WORD_LIST)
    if attempts_left <= max_attempts:
        word = word
    else:
        word = pick_word(WORD_LIST)
    guess = get_guess()

 

def play_game():
    attempts_left = max_attempts
    print(attempts_left)
    if evaluate_guess(attempts_left) == True:
        resp = input('Do you want to play again? y/n')
        if resp == 'y':
            play_game()
        else:
            print('Goodbye')
            exit()

    else:
        attempts_left -= 1
        play_game()



        
play_game()
