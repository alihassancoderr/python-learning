#1. Write a python program to display a user entered name followed by Good 
#Afternoon using input () function.

# name = input("Enter your name:")
# print(f"Good Afternoon {name}")



#3. Write a program to detect double space in a string.
doubbleSpace = "ali  Hassan"
print(doubbleSpace.find("  "))

  
#4. Replace the double space from problem 3 with single spaces. 


doubbleSpace = "ali  Hassan"
print(doubbleSpace.replace("  "," "))


letter = '''  
            Dear <|Name|>, 
            You are selected! 
            <|Date|> 
''' 


print(letter.replace("<|Name|>","Ali").replace("<|Date|>","12/09/2023"))



letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)