a = (2, 3 ,23, 45 ,False, 23,6,9,23,"Roshan" ,'shiba')
b = (45,78,98,0.785)

no =a.count(23)# count total no of 23 ion the touple.
print(no)

print(a.index(23)) #Returns the first index of value x. Raises ValueError if not found

print(a.index(23,6))#index of 23 present after 6th index

print(a[3:5])# slicing - create a new sub touple from original touple last index element is not consider 

print(a+("Rohan",67))#concatinate ("Rohan",67) in the touple a

print(a+b)#concatinate  touple a and b.

a, b, c, d = b
print(a, b, c, d )# unpacking = touple can be unpacking  into individual variable.
