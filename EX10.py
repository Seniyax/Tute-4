import random

hidden=random.randint(1,20)
guess_taken=0

while guess_taken<5:
    Guess=int(input("Guess a number: "))
    guess_taken=guess_taken+1

if Guess==hidden:
        print("correct guess")
else:
        print("wrong guess") 
print("you are out of attempts")           

