f = open("file.txt") # by default 'r' is there
# f = open("file.txt", "r")
print(f.read())
f.close()

# we can write this satement as like this :

with open("file.txt" , "r") as f:
    print(f.read())
    


# we dont have to explicitly close the file. when we use "with" statement. 
