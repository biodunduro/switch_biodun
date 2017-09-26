#This is A Word Guess Game!
print('====THIS IS A WORD GUESS GAME====')
import random

words = ['beautiful', 'handsome', 'pretty', 'smart', 'eloquent']
guess = input('Guess the word i am thinking of: (beautiful/handsome/pretty/smart/eloquent)')

if random.choice(words) == guess:
    print('Correct!')
else:
        count = 0
        while count < 3:
           print(' Wrong! Try again')
           count = count + 1
        else:   
           
            print('Sorry, Wrong! The correct answer is', random.choice(words))

