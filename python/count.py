value = int(input("Enter your Value: "))
result = 0

while value>0:
    value = value // 10
    result= result+1
    print(result,end=" ") 

