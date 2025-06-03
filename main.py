# testing
import random 
from random import randint
from termcolor import colored # pip install termcolor

chosenwords = ["FUZZY", "LUTES", "ANKLE", "PARCH", "ROCKY", "THYME", "DRYAD", "OUGHT", "BORED", "LEANS", "STOMP", "ERASE", "ENDER", "SPEAR", "PRIED", "IRATE", "SCRAP", "CHARM", "SITCH", "SPARK", "QUEEN", "ICHOR", "CRAMP", "LAMPS", "AIRED", "FRIED", "ARISE", "CHORD", "SHANK", "FEAST", "ASHEN"] 
rightguess = False
corrections = [0,0,0,0,0]
imitations = ["O","O","O","O","O"]
correctword = chosenwords[random.randint(0,28)]

count = 0

print("Welcome to wordle! Guess a 5 letter word within 6 tries. Each letter in your word will be marked as correct, in the wrong place, or incorrect. When all the letters in your word match the letters in the correct word, a good job message will be returned. Play.") 

while count <= 5 or rightguess == False:
    guess = input("Guess:")
    if len(guess) != 5: 
        print("Wrong length")
    else: 
        for letter in range(5): 
            if guess[letter] == correctword[letter]:
                corrections[letter] = 2
                count += 1
            elif guess[letter] in correctword:
                corrections[letter] = 1
                count += 1
            else: 
                corrections[letter] = 0
                count += 1 
            if 0 not in corrections or 1 not in corrections:
                rightguess = True 

        print(corrections)#change to imitations

for i in range(5):
    if imitations[i] == 0:
        imitations[i] = imitations[i] # red
    elif imitations[i] == 1:
        imitations[i] = imitations[i] #yellow
    else:
        imitations[i] = imitations[i] #Green

if rightguess == True:
    print('good job')
else:
    print('you lose')