marks ={
    "Riku": 100,
    "Harry": 98,
    "suvam" : 90,
    'list': [1,2,3],
    "Shibu":0,
    90: "Aditya"
}

print(marks.items())#  Returns a list of (key,value)tuples. 
print(marks.keys())#  Returns a list containing dictionary's keys.
print(marks.values())
marks.update({"Harry":99,"Dharmu":95})# update maethod update the values and add new key:values .
print(marks)# Dictionary is mutable. 

print(marks.get("Harry2"))# print None
# print(marks["Harry2"])# return a key error

# my_marks ={}
my_marks = marks.copy() # return a shallow copy of the execting dictionary.
print(my_marks)

marks.clear()# remove all element from the dictionary.
print(marks)

key = [ 'a', 'b', 'c']
new_dict = dict.fromkeys(key,1)# create a new dict. key from 'key link' and assign values 1.
print(new_dict)

print(my_marks.pop("Harry","Default"))# pop the key from dict. and return the value
print(marks.pop("Harry","Default"))# if key is not found then it return Default.
print(my_marks)

print(my_marks.popitem())# remove and rerturn a (key,value) from the dictonary is LIFO element.
print(my_marks)

print(my_marks.setdefault("list","default"))#return the value of key
print(my_marks.setdefault("Samaya","default"))#if key is not present then insert key with default value
print(my_marks)

print(len(my_marks))

