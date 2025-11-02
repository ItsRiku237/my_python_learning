'''4. Write a program to find whether a given username contains less than 10 
characters or not. '''

username = input("Enter your username : ")

if(len(username)<10):
    print("Your username contain less than 10 character .")
else:
    print("Your username contain more than and equal to 10 character .")
    