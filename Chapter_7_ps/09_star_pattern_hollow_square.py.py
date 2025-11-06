'''9. Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * * '''

n = int(input("Enter a number : "))


# for i in range(1,3):
#     if(i==2):
#         for j in range(2,(n-2)+1+1):
#             print("*",end="")
#             print(" "*(n-2),end="")
#             print("*")
#     print("*"*n)

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
