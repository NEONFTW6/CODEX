x = int(input("Enter your number:" ))

print("\n")

if(x == 0 or x==1):
       print(f" {x} number is not a prime number")
      
elif(x > 1):
      
  for i in range(2,x):
      if(x % i) ==0 :
         print(f"{x} number is not a prime number")
         break
  else:
         print(f"{x} is a prime number")
else:
     print(f"{x} is not a prime number")    