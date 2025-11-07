'''2. Write a python program using function to convert Celsius to Fahrenheit. '''
'''
F = ((9/5)*c)+32
C = (F - 32 )*5/9
'''


def temperature(t):
    return (t*(9/5))+32

t = int(input("Enter temperature in Celsius : "))
temp = temperature(t)
print(f"Enter temp. in Fahrenheit is : {round(temp,2)}")