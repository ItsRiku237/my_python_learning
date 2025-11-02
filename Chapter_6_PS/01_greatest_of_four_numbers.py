# 1. Write a program to find the greatest of four numbers entered by the user.
n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))
n4 = int(input("Enter 4th number : "))

if(n1>n2 and n1>n3 and n1>n4):
    print("1st number is the greatest number : ",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("2nd number is the greatest number : ",n2)
elif(n3>n2 and n3>n1 and n3>n4):
    print("3rd number is the greatest number : ",n3)
elif(n4>n2 and n4>n3 and n4>n1):
    print("4th number is the greatest number : ",n4)


