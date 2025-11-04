'''5. Write a program to find the sum of first n natural numbers using while loop. '''

n = int(input("Enter a number : "))
i = 1
add = 0
while(i<=n):
    add +=i
    i +=1
print(f"Sum of first {n} natural number is {add}")