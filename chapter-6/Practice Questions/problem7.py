# 7. Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("Write your post: ")

if("Harry".lower() in post.lower()):
    print("Yes! post is talking about Harry")
else:
    print("No! post is not talking about Harry")