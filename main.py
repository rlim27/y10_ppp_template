# testing
import random 
from random import randint
from colorama import Fore, init
init()
from os import system

chosenwords = ["FUZZY", "LUTES", "ANKLE", "PARCH", "ROCKY", "THYME", "DRYAD", "OUGHT", "BORED", "LEANS", "STOMP", "ERASE", "ENDER", "SPEAR", "PRIED", "IRATE", "SCRAP", "CHARM", "SITCH", "SPARK", "QUEEN", "ICHOR", "CRAMP", "LAMPS", "AIRED", "FRIED", "ARISE", "CHORD", "SHANK", "FEAST", "ASHEN"] 

print("Welcome to wordle! Guess a 5 letter word within 6 tries. Each letter in your word will be marked as correct, in the wrong place, or incorrect. When all the letters in your word match the letters in the correct word, a good job message will be returned. Play.") 

def playround():
    rightguess = False
    corrections = [0,0,0,0,0]
    correctword = chosenwords[random.randint(0,28)]
    imitations = ["","","","",""]
    count = 0

    while count <= 5 and rightguess == False:
        guess = input("Guess:")
        guess = guess.upper()


        if len(guess) != 5: 
            print("Wrong length")
        else: 
            for letter in range(5): 
                numreps = correctword.count(guess[letter])

                if guess[letter] == correctword[letter]:
                    corrections[letter] = 2
                    imitations[letter] = Fore.GREEN + guess[letter]

                elif (guess[letter] in correctword) and (guess.count(guess[letter]) <= numreps):
                    corrections[letter] = 1
                    imitations[letter] = Fore.YELLOW + guess[letter]

                else:
                    corrections[letter] = 0
                    imitations[letter] = Fore.RED + guess[letter]


            print(" ".join(imitations))

            if (not(0 in corrections)) and (not(1 in corrections)):
                rightguess = True 
        
            count += 1
    return rightguess

def verify(rightguess):
    if rightguess == True:
        print('Word Guessed')

    else:
        print('You Ran Out Of Guesses (Lost)')
        
choice = input("Select Menu Option: Play Round = P, Quit = any other key")

while choice in "Pp":
    rightguess = playround()
    verify(rightguess)
    choice = input("Select Menu Option: Play Round = P, Quit = any other key")

print("get out")