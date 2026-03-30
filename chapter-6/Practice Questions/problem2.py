# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
t1 = int(input("Enter your total marks of subject 1: "))
sb1 = int(input("Enter your first subject's marks: "))

t2 = int(input("Enter your total marks of subject 2: "))
sb2 = int(input("Enter your second subject's marks: "))

t3 = int(input("Enter your total marks of subject 3: "))
sb3 = int(input("Enter your third subject's marks: "))

indSbPass1 =33/100*t1
indSbPass2 =33/100*t2
indSbPass3 =33/100*t3

totalMarks = sb1+sb2+sb3


totalPass = 40/100*totalMarks
if(sb1 >= indSbPass1 and sb2>= indSbPass2 and sb3 >= indSbPass3 and totalMarks >= totalPass):
    print("Congratulations you have passed!")
else:
    print("oops! you are cooked hahaha failed")
