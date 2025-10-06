x=int(input("Enter your 1st number: "))
y=int(input("Enter your 2nd number: "))

if x > y:
     z = x
else:
    z = y 

while(True):
    if z % x == 0 and z % y == 0:
         lcm=z
         break
    z += 1
print(f"The LCM of {x} and {y} is: ",lcm)