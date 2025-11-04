'''7. Write a program to print the following star pattern. 
  * 
 *** 
***** for n = 3'''
'''
n= 1        2 gap       1star
n= 2        1 gap       3 star 
n= 3        0 gap       5 star
'''
n = int(input("Enter a number : "))

for i in range(1, n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="") # print statement give a new line by default that reason we use " ,end="" ".
    print("")
