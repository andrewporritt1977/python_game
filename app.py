from Leaderboard import Leaderboard
from Player import Player
import os
import time
import random



class Main:
    os.system('clear')
    print ("********************")
    print ("**  Number Guess  **")
    print ("********************")
    time.sleep(1)

    def game():
        os.system('clear')
        target = random.randint(1,10)
        player = Player(input("Please enter your name - "))
        round = 3

        play_round = input('Would you like to play a round? (y/n)')

        while play_round == 'y':

            i = 0
            while i < round :
                
                try:
                    guess = int(input("Guess my number please?\nIt's between 1 and 10\nYou have " 
                                        + str(3-i) + " guesses left.\nYou are on level - " 
                                        + str(player.score+1) + "\n"))
                    if guess == target :
                        print('\nYou have been successful ' 
                                + player.name + ' the number was ' 
                                + str(target))
                        player.addToScore(1)
                        print('your score is ' + str(player.score))
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
                      
                except (TypeError, ValueError):
                    print("Sorry, numbers only please")
                    continue
                
            print('\nYa done \nThe number you were looking for was ' + str(target))
            play_round = 'n'

        leaderboard = Leaderboard()
        leaderboard.addPlayerToList(player)
        leaderboard.printLeaderBoard()
        play_again = input('Another player (y/n)')
        if play_again == 'y':
            time.sleep(1)
            Main.game()
Main.game()
