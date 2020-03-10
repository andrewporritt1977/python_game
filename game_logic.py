import os
import random

def game_loop():
    player_name = input("Please enter your name - ")
    play_round = input('Would you like to play a round? (y/n)')
    round = 3
    score = 0
    target = random.randint(1,10)
    while play_round == 'y':
        i = 0
        while i < round :
            guess = int(input("Guess my number please " + player_name + "\nIt's between 1 and 10 - "))
            if guess == target :
                print('\nYou have been successful')
                score += 1
                print('your score is ' + str(score) + " ")
                i = 0
                target = random.randint(1,10)
            elif guess < target:
                print('\nHigher')
                i += 1
                continue
            elif guess > target:
                print('\nLower')
                i += 1
                continue
        
        print('\nYa done')
        play_round = 'n'
