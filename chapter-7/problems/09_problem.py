# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 




n = int(input("Enter any number: "))

for i in range(1, n):
    if(i==2):
         print("*",end="")
         print(" ", end="")
         print(" ",end="")
         print(" ", end="")
         print("*")
    print("*",end="")
    print(" ", end="")
    print("*",end="")
    print(" ", end="")
    print("*")
