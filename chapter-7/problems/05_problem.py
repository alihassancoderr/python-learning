# 5. Write a program to find the sum of first n natural numbers using while loop.
# l=[1,2,3,4,5,6,7,8,9,10]
# i=1
# sum=0
# while(i<11):
#     sum += i
#     i += 1
# print(sum)


n = int(input("Enter the number: "))

sum = 0
i = 1
while(i<=n):
    sum += i
    i += 1

print(sum)
    