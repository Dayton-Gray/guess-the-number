import random
import sys
random_number = random.randint(1, 20)  # creates a variable called random number with a range of 1 to 20
guessed_number = ""

while guessed_number != random_number:  # keeps playing code inside till guessed_number = random number
    try:
        guessed_number = input("Guess a whole number between 1 and 20: ")
        if int(guessed_number) < random_number:
            print("Your guess was too low   try again")
        elif int(guessed_number) > random_number:
            print("Your guess was too high try again")
        elif int(guessed_number) == random_number:
            print("Congrats you guessed correctly!")

    except ValueError:  # if you input a string resolves error
        print("Invalid value please type a number ")




