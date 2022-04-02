from random import random

def main():
    print('simulating recquetball')

    # input of the win probability when player werves
    prob_a = float(input('Enter prob of winning a point on the serve of a. '))
    prob_b = float(input('Enter prob of winning a point on the serve of b. '))

    # how many games to simulate
    games = int(input("enter number of games to simulate. "))

    a_wins = 0
    b_wins = 0
    serve = 'A'
    
    # each iteration of this loop represents a game
    for _ in range(games):
        score_a = 0
        score_b = 0
        
        game_over = False
        # this loop runs the length of a game
        while not game_over:
            # start with A serves
            if serve == 'A':
                if random() < prob_a:
                    score_a += 1
                else:
                    serve = 'B'
                    
            if serve == 'B':
                if random() < prob_b:
                    score_b += 1
                else:
                    serve = 'A'
                    
            if score_a == 15:
                a_wins += 1
                game_over = True   
            elif score_b == 15:
                b_wins += 1
                game_over = True
    print("a's winnning percentage", 100 * a_wins / games)
    print("b's winnning percentage", 100 * b_wins / games)
        
main()
