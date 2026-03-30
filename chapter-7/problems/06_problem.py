# 6. Write a program to calculate the factorial of a given number using for loop.
#5! =1*2*3*4*5
# 
n = int(input("Enter any number :"))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(factorial)