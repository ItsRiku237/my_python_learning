'''10. Write a program to print multiplication table of n using for loops in reversed 
order. '''

'''
1 10 =11
2 9
3 8 
4 7
. .
. .
10 1 =11
'''
# method 1
n = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

# method 2
l =[]
for i in range(1,11):
    l.append(i)
l.reverse()
for j in l:
    print(f"{n} X {j} = {n*j}")
01 
