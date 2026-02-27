# By Nathan Nelsen
# Written 2/27/26
# Random Dice


# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():

    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)

    total = roll1 + roll2

    return total

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

total_sum = 0

for i in range(100):
    total_sum += randDice()

average = total_sum / 100

print("Average of the 100 rolls is ", format(average, '.2f')
