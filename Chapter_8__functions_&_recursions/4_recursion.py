#RECURSION 
'''
factorial(n) = n x n-1 x n-2 .....x 3 x 2 x 1
factorial(n) = n x factorial(n-1)

'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

fact = int(input("Enter a number : "))
f = factorial(fact)
print(f"Factorial of {fact} is ",+f)