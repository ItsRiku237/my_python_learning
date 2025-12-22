'''6. Write a program to mine a log file and find out whether it contains ‘python’.'''

with open("log.txt") as f :
    contain = f.read()

if("python" in contain):
    print("Yes , log file contain 'python' .")
else:
    print("No , log file not contain 'python' .")
