#  A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

spamComment = input("Write your comment: ")

# if(spamComment == "buy now" or spamComment == "subscribe this" or spamComment == "click this"):
#     print("This is spam comment")
# else:
#     print("This is not a spam comment")

p1="Make a lot of money"
p2="buy now"
p3="click this"
p4="subscribe this"

if(p1 in spamComment or p2 in spamComment or p3 in spamComment or p4 in spamComment):
    print("spam comment")

else:
    print("not a spam comment")