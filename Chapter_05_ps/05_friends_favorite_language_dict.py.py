'''6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. '''

d = {}

name = input("Enter your name :")
lang = input("Enter your favourite langauge  :")
d.update({name:lang})


d.update({input("Enter your name :"):input("Enter your favourite langauge :")})
d.update({input("Enter your name :"):input("Enter your favourite langauge :")})
d.update({input("Enter your name :"):input("Enter your favourite langauge :")})

print(d)