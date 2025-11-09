'''3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old'''

# Ricz
for i in range(2,21):
    with open(f"Tables/Multiplication_table_{i}","w") as f:
        for j in range(1,11):
            table = f"{i} X {j} = {i*j}\n"
            f.write(table)

# Harry
# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#     with open(f"Tables/Multiplication_table_{n}","w") as f:
#         f.write(table)


# for i in range(2,21):
#     generateTable(i)
