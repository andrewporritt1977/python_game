import os
import time
import random

print ("********************")
print ("**  Number Guess  **")
print ("********************")
time.sleep(2)
os.system('clear')
target = random.randint(1,10)
guess = int(input("Guess my number please?"))

if guess == target :
    print('\nYep')
elif guess < target:
    print('\nHigher')
elif guess > target:
    print('\nLower')
else:
    print('\Try again')
