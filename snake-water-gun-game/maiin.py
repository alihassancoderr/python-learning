#using random funtion to make computer's turn
import random
l = ["snake","water","gun"]
computerNumber = random.randint(0,2)
computerTurn = l[computerNumber].lower()
playerTurn = input("What is your turn: ").lower()

if(playerTurn != "snake" and playerTurn != "gun" and playerTurn != "water"):
    print("invalid choice type snake water or gun")
else:
    if(computerTurn=="snake" and playerTurn =="gun"):
       print("You Won!")
    elif(computerTurn == "snake" and playerTurn == "water"):
        print("Computer Won!")
    elif(computerTurn=="snake" and playerTurn =="snake"):
        print("Tie")
    elif(computerTurn=="water" and playerTurn =="water"):
        print("Tie")
    elif(computerTurn=="water" and playerTurn =="snake"):
        print("You Won!")
    elif(computerTurn=="water" and playerTurn =="gun"):
        print("Computer Won")
    elif(computerTurn=="gun" and playerTurn =="water"):
        print("You Won")
    elif(computerTurn=="gun" and playerTurn =="snake"):
        print("Computer Won")
    elif(computerTurn=="gun" and playerTurn =="gun"):
        print("Tie")




print(f"You Choose {playerTurn}\nComputer Choose {computerTurn}")
