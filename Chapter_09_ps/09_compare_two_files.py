'''9. Write a program to find out whether a file is identical & matches the content of 
another file. '''

with open("log.txt") as f:
    contain_1 = f.read()
    with open("this.txt") as f:
        contain_2 = f.read()
        if(contain_1 == contain_2):
            print("Yes, file 'log.txt' and file 'this.txt' are same .")
        else:
            print("No, file 'log.txt' and file 'this.txt' are not same .")
