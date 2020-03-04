import random

print("Number guessing game!")

randNum = random.randint(1, 100)
guessed = False
for i in range(10):
    if not guessed:
        guess = int(input("Guess a number >> "))
        if guess == randNum:
            print("You guessed it!")
            guessed = True
            break
        elif guess < randNum:
            print("Guess larger")
        elif guess > randNum:
            print("Guess smaller")
if not guessed:
    print("The number was", randNum, "you lose!")

    #  this is a change I am making for the sake of a github test
    #  Test branch



