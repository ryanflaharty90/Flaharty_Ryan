import random

num = random.randint(1, 6)
compNum = random.randint(1, 6)

print("You rolled a", num)

print("The computer rolled a", compNum)


if num > compNum:
    print("You are the winner!")

if num < compNum:
    print("The computer is the winner!")
