import random

lives = 9 

words = ['popular', 'sweater', 'biscuit', 'horizon', 'defiant', 'bladder', 'handout']

secret_word = random.choice(words)
clue = ['_', '_', '_', '_', '_', '_', '_']
heart_symbol = u'\u2764'

guessed_word_correctly = False

print('I\'m looking for a 7-letter word. You have 9 chances to guess, else you\'re dead.') 

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index +1


while lives > 0:
    
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the the whole word: ')


    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('Incorrect. You lose a life')
        lives = lives - 1

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)

else:
    print('You lost! You\'re hanged. The secret word was ' + secret_word)
        