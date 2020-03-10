import os
import time
import random

print ("********************")
print ("**  Number Guess  **")
print ("********************")
time.sleep(2)
os.system('clear')
target = 4

#random.randint(1,10)

player_name = input("Please enter your name - ")
round = 3
score = 0

play_round = input('Would you like to play a round?')

while play_round == 'yes':

    i = 0
    while i < round :
        guess = int(input("Thanks " + player_name + " Guess my number please?"))
        if guess == target :
            print('\nYou have been successful')
            score += 1
            print('your score is ' + str(score) + " " + player_name)
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





# guess = int(input("Thanks " + player_name + " Guess my number please?"))
# if guess == target :
#     print('\nYep')
# elif guess < target:
#     print('\nHigher')
# elif guess > target:
#     print('\nLower')
# else:
#     print('\Try again')
