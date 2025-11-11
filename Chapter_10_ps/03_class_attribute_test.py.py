'''3. Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute? ''' # no it's not changed

class change_or_not:
    a = 10


object = change_or_not()

print(object.a) # here print class attribute bcz instance attribute is not present .\

object.a = 0 # instance attribute is set .

print(object.a) # here print instance attribute bcz instance attribute is present .
print(change_or_not.a) # print class attribute