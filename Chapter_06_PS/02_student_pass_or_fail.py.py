'''2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''

m1 = int(input("Enter Subject 1 mark : "))
m2 = int(input("Enter Subject 2 mark : "))
m3 = int(input("Enter Subject 3 mark : "))

Total_percentage = (100*(m1+m2+m3))/300

if(Total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are passed :",Total_percentage)
else:
    print("You failled : ",Total_percentage)










# if(((m1/50)*100)>=33 and ((m2/50)*100)>=33 and ((m3/50)*100)>=33 and (((m1+m2+m3)/150)*100)>=40):
#     print("Student passed !!")
