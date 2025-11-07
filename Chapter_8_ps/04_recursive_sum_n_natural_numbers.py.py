'''4. Write a recursive function to calculate the sum of first n natural numbers.'''

def sum_n_natural_no(n):
    if(n==1):# recurssive function
        return 1
    else:
        return n+sum_n_natural_no(n-1)



n = int(input("Enter a number : "))
print(sum_n_natural_no(n))
