'''5. Write a program which finds out whether a given name is present in a list or not. '''
list = ["Riku","Aditya","Sangra","Dharmu","Piyush"]

Name = input("Enter a name which find out in the list : ")

if(Name in list):
    print("Enter name is present in the given list .")
else:
    print("Enter name is not present in the given list .")


# if(list[0]==Name or list[1]==Name or list[2]==Name or list[3]==Name or list[4]==Name ):
#     print("Enter name is present in the given list .")
# else:
#     print("Enter name is not present in the given list .")
