'''
Snake = 1
Water = 2
Gun = 3

'''
import random
computer = random.choice([1, 2, 3])

choiceme = input("Enter your choice (s/w/g): ")

if choiceme == "s" or choiceme == "w" or choiceme == "g":
    print()
    
else:
    print("Invalid Choice")
    quit()
    



youDict = { "s" : 1, "w" : 2, "g" : 3 }
reverseyouDict = {1: "Snake", 2: "Water", 3: "Gun" }

you = youDict[choiceme]

print(f"You choose {reverseyouDict[you]} and computer choose {reverseyouDict[computer]}")

if you == computer:
    print("It's a tie!")
else:
    if( you == 1 and computer == 2 ):
        print("You Win!")

    elif ( you == 1 and computer == 3 ):
        print("You Lose!")
    
    elif( you == 2 and computer == 1 ):
        print("You Lose!")
    
    elif ( you == 2 and computer == 3 ):
        print("You Win!")
    
    elif ( you == 3 and computer == 1 ):
        print("You Win!")
    
    elif( you == 3 and computer == 2 ):
        print("You Lose!")

    else:
        print("Something went wrong!")
