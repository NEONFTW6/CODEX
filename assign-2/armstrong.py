x=int(input("Enter your number to check if it is armstrong number or not: "))


num=len(str(x))
sum=0
original=x
while x>0:
    sum += (x%10) ** num
    x=x//10
if original == sum:
    print("The given number is armstrong number")
else:
    print("The given number is not armstrong number")

   