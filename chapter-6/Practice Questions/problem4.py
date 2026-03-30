# Write a program to find whether a given username contains less than 10 
# characters or not. 

userName = input("Enter your username")

if(len(userName) < 10):
    print("less than 10")
else:
    print("Not less than 10")