
WORD_LIST = ['biodun', 'bayo', 'ben', 'tomi', 'chidera', 'affiong', 'effiong', 'james']
max_attempts = 5


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
    word = pick_world(WORD_LIST)
    guess = get_guess()
    if word != guess:
        count = 0
        while (count < 5):
            print ('The count is:', count)
            print('Your guess is wrong! Guess again')
        guess = get_guess()
        count = count + 1
    else:
        print('Goodbye')
        exit()


evaluate_guess()




##
##def play_game():
##    
##    if evaluate_guess() == True:
##        resp = input('Do you want to play again? y/n')
##        if resp == 'y':
##            play_game()
##        else:
##            print('Goodbye')
##            exit()
##
##    else:
##        attempts_left -= 1
##        play_game()
##
##
##
##        
##play_game()
##
##


