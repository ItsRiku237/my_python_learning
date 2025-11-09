'''4. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. '''

# Ricz
with open("poems.txt") as f:
    content = f.read()
    if("Donkey" in content):
        newContent = content.replace("Donkey","#####")
        with open("poems.txt","w") as f:
            f.write(newContent)

# Harry
# word = "Donkey"
# with open("poems.txt") as f:
#     content = f.read()

# newContent = content.replace(word,"#####")

# with open("poems.txt","w") as f:
#     f.write(newContent)