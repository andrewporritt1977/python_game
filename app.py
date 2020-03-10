from Leaderboard import Leaderboard
from Player import Player
import os
import time
import random

print ("********************")
print ("**  Number Guess  **")
print ("********************")
time.sleep(2)
os.system('clear')
target = random.randint(1,10)



player = Player(input("Please enter your name - "))
round = 3

play_round = input('Would you like to play a round?')

while play_round == 'yes':

    i = 0
    while i < round :
        guess = int(input("Thanks " + player.name + " Guess my number please?"))
        if guess == target :
            print('\nYou have been successful')
            player.addToScore(1)
            print('your score is ' + str(player.score) + " " + player.name)
            round = 3
 
        elif guess < target:
            print('\nHigher')
            i += 1
            continue
        elif guess > target:
            print('\nLower')
            i += 1
            continue
    
    print('\nYa done')
    play_round = 'no'

leaderboard = Leaderboard()
leaderboard.addPlayerToList(player)
leaderboard.printLeaderBoard()



# guess = int(input("Thanks " + player_name + " Guess my number please?"))
# if guess == target :
#     print('\nYep')
# elif guess < target:
#     print('\nHigher')
# elif guess > target:
#     print('\nLower')
# else:
#     print('\Try again')
