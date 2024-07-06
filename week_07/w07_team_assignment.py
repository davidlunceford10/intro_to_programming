import random

magic_number = random.randint(1,10)
guess_number = None

while guess_number != magic_number or guess_number == None :
    guess_number = int(input('What is your guess? '))
    if guess_number > magic_number:
        print("Lower")
    elif guess_number < magic_number:
        print("Higher")

print("You guessed it!")