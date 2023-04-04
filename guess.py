import random

print("Welcome to the guessing game")

playing = input("Do you wanna play the game? ")
if playing.lower() != 'yes':
    quit()
else:
    print("Let's start")

top_number = input("Choose a top number: ")
if top_number.isdigit():
    top_number = int(top_number)
    if top_number<=0:
        print("Please input a number greater than zero")
        quit()
else:
    print("Please input a number")
    quit()

random_number = random.randint(0, top_number)

guesses=0

while True:
    guesses+=1
    guess_user = input("Make a guess: ")
    if guess_user.isdigit():
        guess_user = int(guess_user)

    elif guess_user[0]=='-':
        print("Please input a number greater than zero next time")
        continue
    else:
        print("Please a input a number next time")
        continue


    if guess_user == random_number:
        print("You guessed it right!")
        break
    elif guess_user>random_number:
        print("Your guess is greater than the random number")
    else:
        print("Your guess is lesser than the random number")


if guesses==1:
    print(f"You guessed in {guesses} try")
else:
    print(f"You guessed in {guesses} tries")