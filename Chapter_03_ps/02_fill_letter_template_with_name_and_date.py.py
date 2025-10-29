# 2. Write a program to fill in a letter template given below with name and date. 
letter = '''
       Dear <|Name|>, 
     You are selected! 
      <|Date|> 
        '''
#".Replase" use for chain the function to impliment again in the same string.
print(letter.replace("<|Name|>","Riku").replace("<|Date|>","01 January 2027"))
print(letter)# string are immutable .