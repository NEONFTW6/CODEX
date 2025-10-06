import sys

print("""Select the option for calculation from below: 
print("1.Addition")
print("2.Substraction")
print("3.Multiplication""")
print(" ")

User_input = int(input("Enter the choice: "))
if User_input not in (1,2,3):
    print("Invalid choice")
    sys.exit() 
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

addition = a+b
substraction = a-b
multiply = a*b

if User_input == 1:
   print(f"The addition is {a} and {b} is :",addition)
elif User_input == 2:
    print(f"The substraction is {a} and {b} is :",substraction)    
else:
    print(f"The multiplication is {a} and {b} is :",multiply)


