for i in range(6):
    print(i)
    
for i in range(0,5):
    print(i)

for i in range(0,50,5):# range(start, stop, step_size) 
    print(i)

# for loop with list
print("for loop with list :")
l = ["Ricz",1,"Ribby","chiku",0,True]
for i in l:
    print(i)

# for loop with touple
print("for loop with touple :") 
t = (12 , "saleem ", "Rajwant")
for i in t:
    print(i)

# for loop with string
print("for loop with string :")
s ="Ribby"
for i in s:
    print(i)

#FOR LOOP WITH ELSE 
print("FOR LOOP WITH ELSE :")
l= [1,7,8] 
for item in l: 
    print(item) 
else: 
    print("done") # this is printed when the loop exhausts!

#THE BREAK STATEMENT 
print("THE BREAK STATEMENT :")
for i in range(25):
    if(i==11):
        break
    print(i)

# THE CONTINUE STATEMENT
print("THE CONTINUE STATEMENT :")
for i in range(10):
    if(i==5):
        continue
    print(i)

# PASS STATEMENT 
print("PASS STATEMENT :")
l = [1,7,8]
for item in l: 
    pass # without pass, the program will throw an error 
n= 0
while(n<5):
    print("JNV")
    n +=1