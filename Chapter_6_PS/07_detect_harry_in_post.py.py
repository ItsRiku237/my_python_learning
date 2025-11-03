'''7. Write a program to find out whether a given post is talking about “Harry” or not.'''

# post = "Harry"

Given_post = input("Enter post : ")

# if("Harry".lower() in Given_post.lower()):

if("harry" in Given_post.lower()):
    print("Yes,Given post is talking about Harry.")
else:
    print("No,Given post is not talking about Harry.")