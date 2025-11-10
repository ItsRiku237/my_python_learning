'''7. Write a program to find out the line number where python is present from ques 6.'''

#ricz(f.line())
# line_no = 1
# with open("log.txt") as f:
#     line = f.readline()
#     while(line != ""):
#         if("python" in line):
#             print(f"Line no : {line_no}")
#         line = f.readline()
#         line_no += 1


# harry (f.lines())
with open("log.txt") as f:
    lines = f.readlines()
    line_no =1
for line in lines:
    if("python" in line):
        print(f"Yes, 'python' is present in line no : {line_no}")
    line_no +=1