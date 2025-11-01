'''2. Write a program to input eight numbers from the user and display all the unique 
numbers (once). 
'''
s = set()

s1 = int(input("Enter 1st number :"))
s.add(s1)

s2 =input("Enter 2nd number :")
s.add(int(s2))

s.add(int(input("Enter 3rd number :")))
s.add(int(input("Enter 4th number :")))
s.add(int(input("Enter 5th number :")))
s.add(int(input("Enter 6th number :")))
s.add(int(input("Enter 7th number :")))
s.add(int(input("Enter 8th number :")))
print(s)