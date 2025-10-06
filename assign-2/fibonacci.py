def fibonacci(x):
 if x<=1:
  return x
 else:
  return fibonacci(x-1)+fibonacci(x-2)

x=int(input("Enter your Febonacci number: ")) 
print("The fibonacci sequence is: ")

for i in range(x+1):
    print(fibonacci(i))