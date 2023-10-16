import random
a = random.randint(1,5)
userchoice = int(input("choose a number between 1 and 5.........."))
if userchoice == a:
    print("You guessed right")
else:
    if userchoice < a:
        print("You guessed too low")
    else:
        print("You guessed too high")
