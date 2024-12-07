dice rolling game (first project)

import random

while True:
    choice = input("do you want to roll dice (y/n) : ").lower()
if choice == "y":
    dice1=(random.randint(1, 6))
    dice2=(random.randint(1, 6))
    print({dice1},{dice2})
elif choice == "n":
    print("thanks for playing ")

else :
    ("invalid choice please try again ")



