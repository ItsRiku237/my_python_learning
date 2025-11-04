'''4. Write a program to find whether a given number is prime or not. '''
n = int(input("Enter a number for check prime or not : "))

for i in range(2,n):
    if(n%i==0):
        print("Enter number is not a prime number .")
        break
else:
    print("Enter number is a prime number .")
#when for loop are exusted without break statement then else statement is executed.\
