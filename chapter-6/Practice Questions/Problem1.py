# 1. Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))
n4 = int(input("Enter number: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("greatest number is: ",n1)
if(n2>n1 and n2>n3 and n2>n4):
    print("greatest number is: ",n2)
if(n3>n1 and n3>n2 and n3>n4):
    print("greatest number is: ",n3)
if(n4>n1 and n4>n2 and n4>n3):
    print("greatest number is: ",n4)

