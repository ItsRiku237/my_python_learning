a = int(input("Enter Your age : "))


# if statement no 1:
if(a%2==0):
    print("Enter age is a Even number.")

# if statement no 2:
if(a>=18 and a<60):
    print("You are a adult person.")
elif(a>60):
    print("You are a old person.")
elif(a>0 and a<18):
    print("You are not a adult person.")
else:
    print("Enter a valid age !!")

# end the program.
print("End of program !!")
