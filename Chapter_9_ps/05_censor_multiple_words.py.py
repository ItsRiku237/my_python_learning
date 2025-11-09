'''5. Repeat program 4 for a list of such words to be censored.'''
'''4. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. '''

words = ["Donkey","Dog" ,"Elephant", "Monkey"]

with open("poems.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word,"#" * len(word))
    
with open("poems.txt", "w") as f:
    f.write(content)