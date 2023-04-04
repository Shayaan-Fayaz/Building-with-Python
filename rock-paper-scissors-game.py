import random

computer_wins =0 
user_wins=0
draw_times = 0

options = ['rock', 'paper', 'scissor']


while True:
    user_guess = input("Pick 'rock', 'paper', 'scissor' or press Q to quit: ").lower()

    if user_guess=='q':
        break

    if user_guess not in options:
        print("Not a valid input")
        continue

    random_number = random.randint(0, 2)
    computer_guess = options[random_number]

    print(f"Computer picked {computer_guess}.")

    if user_guess==computer_guess:
        print(f"You and computer both picked {user_guess}")
        draw_times+=1
        continue

    if user_guess=='rock' and computer_guess=='scissor':
        print("You won!, coz computer picked 'scissor'")
        user_wins+=1
        continue
    elif user_guess=='rock' and computer_guess=='paper':
        print("You lost! coz computer picked 'paper'")
        computer_wins+=1
        continue

    if user_guess=='paper' and computer_guess=='rock':
        print("You won!, coz computer picked 'rock'")
        user_wins+=1
        continue
    elif user_guess=='paper' and computer_guess=='scissor':
        print("You lost! coz computer picked 'scissor'")
        computer_wins+=1
        continue

    if user_guess=='scissor' and computer_guess=='paper':
        print("You won!, coz computer picked 'paper'")
        user_wins+=1
        continue
    elif user_guess=='scissor' and computer_guess=='rock':
        print("You lost! coz computer picked 'rock'")
        computer_wins+=1
        continue


print(f"You won {user_wins} times. Computer won {computer_wins} times. Total draws are {draw_times}.")