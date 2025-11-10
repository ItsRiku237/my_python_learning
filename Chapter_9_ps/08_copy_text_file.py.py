'''8. Write a program to make a copy of a text file “this. txt” '''

# long method
# f = open("log.txt")
# contain = f.read()
# g = open("this.txt","w")
# g.write(contain)
# g.close()
# f.close()


# f = open("log.txt")
# contain = f.read()
# f = open("this.txt","w")
# f.write(contain)
# f.close()
# f.close()

with open("log.txt") as f:
    contain = f.read()
    
with open("this.txt","w") as f:
        f.write(contain)
    