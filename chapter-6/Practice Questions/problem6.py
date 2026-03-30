# Write a program to calculate the gradee of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50   => F      



marks = int(input("Enter your marks: "))

if(marks >= 90 and marks <=100):
    print("You got grade 'Ex' with marks ",marks)

elif(marks >= 80 and marks <=90):
    print("You got grade 'A' with marks ",marks)

elif(marks >= 70 and marks <=80):
    print("You got grade 'B' with marks ",marks)

elif(marks >= 60 and marks <=70):
    print("You got grade 'C' with marks ",marks)

elif(marks >= 50 and marks <=60):
    print("You got grade 'D' with marks ",marks)

elif(marks < 50):
    print("You got grade 'F' with marks ",marks)