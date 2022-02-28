import random
import math

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

tries = round(math.log(upper - lower + 1, 2))
ran = random.randint(lower, upper)
print("You have ", tries, " chances")

try:
    while True:
        if tries != 0:
            num = int(input("Enter your guess: "))
            if num > ran:
                print("Try Again! You guessed too high")
                tries -= 1
            elif num < ran:
                print("Try Again! You guessed too small")
                tries -= 1
            else:
                print("Congratulations! You did it in ", tries, " tries")
                break
        else:
            print("Better Luck Next Time!")
            break

except ValueError:
    print("You must enter an integer")