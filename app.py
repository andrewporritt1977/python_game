import os
import time
import random

print ("********************")
print ("**  Number Guess  **")
print ("********************")
time.sleep(2)
os.system('clear')
target = random.randint(1,10)
player_name = input("Please enter your name - ")
round = 3
score = 0

i = 0
while i < round :
    guess = int(input("Thanks " + player_name + " Guess my number please?"))
    if guess == target :
        print('\nYou have been successful')
        score+=1
        print('your score is ' + str(score) + " " + player_name)
        break
    elif guess < target and i < round:
        print('\nHigher')
        i += 1
        continue
    elif guess > target and i < round:
        print('\nLower')
        i += 1
        continue
    elif i == round :
        print('\nYa done')
        break



# guess = int(input("Thanks " + player_name + " Guess my number please?"))
# if guess == target :
#     print('\nYep')
# elif guess < target:
#     print('\nHigher')
# elif guess > target:
#     print('\nLower')
# else:
#     print('\Try again')
