print("Welcome to the quiz")

do_you = input("Do you want to play the game (yes/no): ").lower()

if do_you != "yes":
    quit()
else:
    print("Let's do it")

score=0

answer = input("What is the capital of India ")
if answer.lower() == "new delhi":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the capital of Italy ")
if answer.lower() == "rome":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the capital of Germany ")
if answer.lower() == "berlin":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the capital of USA ")
if answer.lower() == "washington dc":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the capital of Canada ")
if answer.lower() == "ottawa":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"You got {score} questions right")
print(f"You score is {(score/5)*100}")