'''6. Write a python function which converts inches to cms.'''
'''1inch = 2.54cm'''

def inch_cm(x):
    return x*2.54

n = int(input("Enter a number : "))
print(f"{n} inches is equal to ",+inch_cm(n))