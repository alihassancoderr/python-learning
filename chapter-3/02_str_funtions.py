#here we will study funtions of string

#first func is """len""" it tell us length of string
name = "alihassan"

print(len(name))

# second funtion is """endswith""" and it tell us
# whether this string end with our given letters or not

print(name.endswith("an"))


# third funtion is """startswith""" and it tell us
# whether this string start with our given letters or not

print(name.startswith("ali"))

#captalize it will captalize first letter of word

print(name.capitalize())

#count it will count how many times a letter occur in a word

print(name.count("s"))

#string.find(word) – This function friends a word and returns the index of first 
#occurrence of that word in the string.

print(name.find("h"))
print(name.find("ss"))


#string.replace (old word, new word ) – This function replace the old word with 
#new word in the entire string. 


print(name.replace("hassan", "khan"))



print(name.upper()) #it will convert all letters to upper case
print(name.lower()) #it will convert all letters to lower case