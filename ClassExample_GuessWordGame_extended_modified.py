
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

##
##def evaluate_guess(attempts_left):
##    guess = get-guess()
##    word = ' '
##    if attempts_left == 5:
##        word = pick_word(WORD_LIST)
##        guess == word
##        print('Your guess is correct!')
##        resp = input('Do you want to play again? y/n')
##        if resp == 'y':
##            word = pick_word(WORD_LIST)
##            attempts_left -= 1
##        else:
##            attempts_left -= 1
##            print('Wrong guess')
##            guess = get_guess()
##            evaluate_guess(attempts_left)
##
##
##
##    else:
##        word = pick_word(WORD_LIST)
##    guess = get_guess()



def evaluate_guess(word, attempts):
     while attempts > 0:
         guess = get_guess()
         if guess != word:
             attempts -= 1
             print('Wrong attempt, you have', attempts, 'attempts left')
             evaluate_guess(word, attempts)
    
         else:
            print('Your guess is correct')
            return True
            # break
            
        
     else:
        print('You have used up your attempts!')
        return False
    
     

##def evaluate_guess(word, attempts):
##     while attempts > 0:
##         guess = get_guess()
##         if guess != word:
##             attempts -= 1
##             print('Wrong attempt, you have', attempts, 'attempts left')
##
##             evaluate_guess(word, attempts)
##    else:
##        print('Your guess is correct')
##        return True
##        
##    else:
##        print('You have used up your attempts!')
##        return False






     

##def play_game():
##    attempts_left = max_attempts
##    print(attempts_left)
##    if evaluate_guess(attempts_left) == True:
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

def play_game(game_count):
    game_count += 1
    word = pick_word(WORD_LIST)
    print('Welcome to Word Guess Game')
    print()

    while evaluate_guess(word, 5):
        ask = input('Do you want to continue y/n')
        if ask == 'y':
            
            play_game(game_count)
        else:
            print('You played,', game_count, 'games')
            print('Goodbye')
            exit()

    else:
        print('Oops, you missed that one')
        retry = input('Do you want to try another word? y/n')
        if retry == 'y':
            play_game(game_count)
        else:
            print('Goodbye')




play_game(0)
        
    





