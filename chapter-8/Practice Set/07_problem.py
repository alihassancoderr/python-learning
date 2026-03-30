l = ["hassan","shan","hamza"]
def removeWord(l,word):
    for i in l:
        if (word == i):
            l.remove(word)
            return l

removeWord(l,"hassan")
print(l)