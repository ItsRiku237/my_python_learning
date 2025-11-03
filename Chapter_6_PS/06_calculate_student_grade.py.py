'''6. Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50        
=> F'''

marks = int(input("Enter your mark : "))

if(marks>90 and marks<=100):
    print("According to your mark your Grade is : Ex")
elif(marks>80 and marks<=90):
    print("According to your mark your Grade is : A")
elif(marks>70 and marks<=80):
    print("According to your mark your Grade is : B")
elif(marks>60 and marks<=70):
    print("According to your mark your Grade is : C")
elif(marks>50 and marks<=60):
    print("According to your mark your Grade is : D")
elif(marks<=50):
    print("According to your mark your Grade is : F")
else:
    print("Enter a valid mark in between 0 to 100 .")