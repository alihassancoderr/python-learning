# 8. Write a python function to print multiplication table of a given number.

def multiplication (number):
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
multiplication(int(input("Enter any number")))