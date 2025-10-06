N1=str(input("Enter the student name: \n"))
r1=int(input("Enter the roll number: \n"))
print("\n")
sub1=int(input("Enter mark of Maths:\n"))
sub2=int(input("Enter mark of Physics:\n"))
sub3=int(input("Enter mark of Chemistry: \n"))
print("\n")
total=sub1 + sub2 + sub3
print("The total marks are: ",total)
print("\n")
perc=total/3 
print("The percentage is: ",+perc)
print("\n")
if(perc > 90):
    print("Grade A")

elif(perc > 70):
    print("Grade B")

elif(perc > 50):
    print("Grade C")    

elif(perc > 30):
    print("Grade D")

else:
    print("Fail")

