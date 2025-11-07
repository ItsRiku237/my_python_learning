'''5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 '''

# def pattern(n):
#     for i in range(1,n+1):
#         # print("*"*(4-i))
#         print("*"*((n+1)-i))

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

n = int(input("Enter a number : "))
pattern(n)
