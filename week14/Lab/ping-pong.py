# Jingbo Wang
# ping-pong.py
# A program to play a BO5 ping-pong ball game

from random import random

def main():
    printIntro()
    probA, probB = getInputs()
    winsA, winsB, win_servesA, win_servesB = simNGames(probA, probB)
    printSummary(winsA, winsB, win_servesA, win_servesB)

def printIntro():
    print("This program simulates a game of ping-pong ball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # returns the two simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    return a, b

def simNGames(probA, probB):
    # Simulates n games of ping-pong ball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    win_roundsA =[] # To store each round for A
    win_roundsB =[] # To store each round for B
    for i in range(5):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
            win_roundsA.append('W') # A wins this serve
            win_roundsB.append('-') # B lose this serve
        else:
            winsB = winsB + 1
            win_roundsA.append('-') # A lose this serve
            win_roundsB.append('W') # B wins this serve
        if winsA == 3 or winsB == 3:
            break
    return winsA, winsB, win_roundsA, win_roundsB

def simOneGame(probA, probB):
    # Simulates a single game or ping-pong ball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # A and B represent scores for a ping-pong ball game
    # Returns Ture if the game is over, False otherwise.
    return a==11 or b==11

def printSummary(winsA, winsB, win_roundsA, win_roundsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    
    if winsA == 3:
        print("A is winner") # A is winner if A wins 3 serves
    else:
        print("B is winner") # B is winner if B wins 3 serves
    # the total win serves for A and B
    print("Wins for A: {0}".format(winsA))
    print("Wins for B: {0}".format(winsB))
    
    # each rounds for A and B
    print("A: ", *win_roundsA)
    print("B: ", *win_roundsB)
main()
