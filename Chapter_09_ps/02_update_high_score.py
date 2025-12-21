'''2. The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score.'''

'''import random

def game():
    n = random.randint(1,100)
    return n
score = game()
with open("Hi-score.txt","r") as f:
    if(f.read()==""):
        print("There is no higest score !!")
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    else:
        with open("Hi-score.txt","r") as f:
            hi_score = int(f.read())
            if(score > hi_score):
                with open("Hi-score.txt","w") as f:
                    f.write(str(score))
                    print("You score is higest :",score)
            else:
                print(f"your score {score} is not higest higest , higest score is :",hi_score)
        '''

'''import random

def game():
    score = random.randint(1,100)
    with open("Hi-score.txt") as f:
        Hi_score = f.read()
        if(Hi_score != ""):
            Hi_score = int(Hi_score)
        else:
            Hi_score = 0
    
    print(f"Your score is {score} and High Score is {Hi_score}.")
    with open("Hi-score.txt","w") as f:
        if(score>=Hi_score):
            f.write(str(score))
            print(f"Your score {score} is higest .")
        else:
            f.write(str(Hi_score))
            print(f"Your score {score} is not higest !!")

    return score

game()'''


import random

def game():
    print("You are playing a game !!")
    score = random.randint(1,100)
    with open("Hi-score.txt") as f:
        Hi_score = f.read()
        if(Hi_score != ""):
            Hi_score = int(Hi_score)
        else:
            Hi_score = 0
    
    print(f"Your score is {score}.")
    if(score>=Hi_score):
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
           

    return score

game()

