'''1. Write a program to print multiplication table of a given number using for loop.'''

n = int(input("Enter the no for multiplication : "))
for i in range(1,11):
    # x = n*i
    # print( n," * ", i ,"= ",x)
    print(f"{n} X {i} = {n*i}")
