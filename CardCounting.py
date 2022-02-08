import time
import random

CARDS = [
    '2', '2', '2', '2', 
    '3', '3', '3', '3', 
    '4', '4', '4', '4', 
    '5', '5', '5', '5', 
    '6', '6', '6', '6', 
    '7', '7', '7', '7', 
    '8', '8', '8', '8', 
    '9', '9', '9', '9', 
    '10', '10', '10', '10', 
    'J', 'J', 'J', 'J', 
    'Q', 'Q', 'Q', 'Q', 
    'K', 'K', 'K', 'K', 
    'A', 'A', 'A', 'A'
]



# difficulty: 1 = Hard; 2 = Medium; 3 = Easy
def run(speed, decks):
    count = 0
    numCardsSeen = 0

    newCards = []

    for i in range(decks):
        newCards = CARDS + newCards

    random.shuffle(newCards)

    seenCards = []

    for i in newCards:
        if numCardsSeen == 48:
            break
        print(i)
        if i == '2': 
            count+=1
        elif i == '3':
            count+=1
        elif i == '4':
            count+=1
        elif i == '5':
            count+=1
        elif i == '6':
            count+=1
        elif i == '10':
            count-=1
        elif i == 'J':
            count-=1
        elif i == 'Q':
            count-=1
        elif i == 'K':
            count-=1
        elif i == 'A':
            count-=1
        
        numCardsSeen+=1

        seenCards.append(i)

        time.sleep(speed)
    
    print('Running Count: ', count)
    print('True Count:', count/decks)

run(3, 1)