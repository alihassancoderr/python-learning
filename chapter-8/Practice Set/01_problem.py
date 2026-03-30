# 1. Write a program using functions to find greatest of three numbers.

def greatest (n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3

number1 = int(input("Enter first number: "))
number2 = int(input("Enter first number: "))
number3 = int(input("Enter first number: "))
number = greatest(number1,number2,number3)
print(number)