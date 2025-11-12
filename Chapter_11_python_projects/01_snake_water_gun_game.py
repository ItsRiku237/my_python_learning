'''PROJECT 1: SNAKE, WATER, GUN GAME 
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user.'''
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choise : ")
if(youstr=="s" or youstr=="w" or youstr=="g"):
    youDict = {"s":1 ,"w":-1 ,"g":0}
    youChoice = youDict[youstr]
    revDict = {1:"Snake",-1:"Water" ,0:"gun"}

    print(f"Computer choose {revDict[computer]}.\nYou choose {revDict[youChoice]}.")

    if(computer==youChoice):
        print("Draw!!")
    else:
        if(computer==1 and youChoice==-1): # computer - you = 2
            print("You lose!")
        elif(computer==1 and youChoice==0): # computer - you = 1
            print("You win!")
        elif(computer==-1 and youChoice==0): # computer - you = -1
            print("You lose!")
        elif(computer==-1 and youChoice==1): # computer - you = -2
            print("You win!")
        elif(computer==0 and youChoice==1): # computer - you = -1
            print("You lose!")
        elif(computer==0 and youChoice==-1): # computer - you = 1
            print("You win!")

        # shorted method
        # if(computer-youChoice ==-1 or computer-youChoice==2):
        #     print("You lose!")
        # else:
        #     print("You win!")


else:
    print("Somthing went wrong!! Please choose s , w and g .")


