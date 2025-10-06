x=int(input("Enter your 1st number: "))
y=int(input("Enter your 2nd number: "))

if x < y:
     z = x
else:
    z = y 

for i in range(1,z+1):
      if x % i == 0 and y % i == 0:
       hcf = i
print(f"The HCF of {x} and {y} is: ",hcf)

