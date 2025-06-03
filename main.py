# testing
import random 

from random import randint 

chosenwords = ["FUZZY", "LUTES", "ANKLE", "PARCH", "ROCKY", "THYME", "DRYAD", "OUGHT", "BORED", "LEANS", "STOMP", "ERASE", "ENDER", "SPEAR", "PRIED", "IRATE", "SCRAP", "CHARM", "SITCH", "SPARK", "QUEEN", "ICHOR", "CRAMP", "LAMPS", "AIRED", "FRIED", "ARISE", "CHORD", "SHANK", "FEAST", "ASHEN"] 
rightguess = False 
corrections = [0,0,0,0,0] 
imitations = ["OOOOO"] 
correctword = chosenwords[random.randint(0,28)] 
count = 0 

print("Welcome to wordle! Guess a 5 letter word within 6 tries. Each letter in your word will be marked as correct, in the wrong place, or incorrect. When all the letters in your word match the letters in the correct word, a good job message will be returned. Play.") 

while count <= 5 or rightguess == False: 
    guess = input("Guess:") 
    if len(guess) != 5: 
        print("Wrong length") 

    else: 
        for letter in range(4): 
            if guess[letter] == correctword[letter]: 
                imitations[letter] = guess[letter] #GREEN 
                corrections[letter] == 2 
            elif guess[letter] in correctword: 
                imitations[letter] = guess[letter] #YELLOW 
                corrections[letter] == 1 
            else: 
                imitations[letter] = guess[letter] #RED 
                corrections[letter] == 0 
                count += 1 
            print(imitations) 
if 0 not in corrections or 1 not in corrections: 
    correctguess = True 
if correctguess == True: 
    print('good job') 
else: 
    print('lose') 