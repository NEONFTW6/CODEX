# Factorial

n = int(input("Enter your number: "))
result = 1

for i in range(2,n+1):
    result = result*i
    print(result)
    
    
# Factorial using math library    
# import math 
# num = int(input("Enter your number: "))
# result = math.factorial(num)
# print(result)