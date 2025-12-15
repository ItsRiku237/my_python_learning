'''3. Attempt problem 1 using while loop. '''
'''1. Write a program to print multiplication table of a given number using for loop.'''

n = int(input("Enter the no for multiplication : "))
x = 1
while(x<=10):
    print(f"{n} X {x} = {n*x}")
    x +=1

# for i in range(1,11):
#     # x = n*i
#     # print( n," * ", i ,"= ",x)
#     print(f"{n} X {i} = {n*i}")
