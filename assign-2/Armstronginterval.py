x=int(input("Enter your 1st number "))
y=int(input("Enter your 2nd number "))

print("\n")

print(f"The armstrong numbers between {x} and {y} are: ")
for i in range(x,y+1):
     digit=str(i)
     num=len(digit)
     sum=0
     for j in digit:
         sum +=int(j) ** num    
     if sum==i:
         print(i)
    
   