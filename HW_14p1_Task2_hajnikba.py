# Activity Python 1: HW14.1: Python Repetition (Task 2)
# File:  HW_14p1_Task2_hajnikba
# Date:    30 11 22
# By:      Bryce Hajnik
# Section: 011
# Team:    156
# 
# ELECTRONIC SIGNATURE
# Bryce Hajnik
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# Simulates a two player dice game
import random
PlayerTurn = 0
Player1SCORE = 0
Player2SCORE = 0
print('PLAYER 1 ROLL YOUR DICE!')
print(' ')
while Player1SCORE < 50 and Player2SCORE < 50:
    if PlayerTurn % 2 == 0:
        D1 = random.randint(1,6)
        D2 = random.randint(1,6)
        print('DICE ONE IS...' ,D1, 'AND DICE TWO IS...', D2)
        if D1 == 5 or D2 == 5:
            print('PLAYER 1, YOUR TURN IS OVER')
            print(' ')
            print('PLAYER 2 YOU MAY NOW BEGIN')
            print(' ')
            PlayerTurn += 1
        else:
            Player1SCORE += D1 + D2
            print('PLAYER 1 YOUR SCORE IS', Player1SCORE)
    else:
        D1 = random.randint(1,6)
        D2 = random.randint(1,6)
        print('DICE ONE IS...' ,D1, 'AND DICE TWO IS...' ,D2)
        if D1 == 5 or D2 == 5:
            print('PLAYER 2, YOUR TURN IS OVER')
            print(' ')
            print('PLAYER 1 YOU MAY NOW BEGIN')
            print(' ')
            PlayerTurn += 1
        else:
            Player2SCORE += D1 + D2
            print('PLAYER 2 YOUR SCORE IS', Player2SCORE)

print(' ')
if Player1SCORE > Player2SCORE:
    print('AND THE WINNER IS...PLAYER 1!')
else:
    print('AND THE WINNER IS...PLAYER2!')
print('Player 1 Score Is:' , Player1SCORE)
print('Player 2 Score IS:' , Player2SCORE)
          
            
