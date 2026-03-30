# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.

n = int(input("Enter any number: "))
nn=10
for i in range(1,11):
    print(f"{n}x{nn} = {n * nn}")
    nn -= 1
