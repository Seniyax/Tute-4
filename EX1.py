import random



 

Hidden=random.randint(1,20)
Guess=int(input("Guess a number between 1 to 20 : "))



while Guess != Hidden:

    Guess=int(input("Guess a number between 1 to 20 : "))

print("you re correct") 
print(Guess and Hidden)    