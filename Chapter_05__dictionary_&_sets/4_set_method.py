s = {1, 25, 3, 89 , 1, 3, 3, 3 ,98 , "Riku"}

print(s,len(s))

s.add(000)
print(s)

s.remove(1)
print(s)

# s.pop() # remove a random element
print(s.pop())
print(s)

s1={2,3,45,68,55,11}
s2={65,85,30,47,3,45,111}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1-s2)
# print(s2-s1)

print(s2.difference(s1)) # print(s2-s1) is thios same as s2.difference(s1)

print({2,45}.issubset(s1))

print(s1.issubset({4,78,98,3,2,4}))

print(s1.issuperset({45,2,11}))

s1.clear()
print(s1)