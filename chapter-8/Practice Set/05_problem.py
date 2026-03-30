# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

def starPattern (n):
    if(n==0):
        return
    print("*"*n)
    starPattern(n-1)
starPattern(5)
    