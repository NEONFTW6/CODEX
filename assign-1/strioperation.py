print("1,concatinate: \n")

x="mango"
print("First word is:",x)
y= " is tasty"
print("Second word is:",y)

print("Result: \n")

result =x + y
print(result)
print("\n")

print("2,slice the mango range 3: ")
print("Result: \n")
a=slice(3)
print(x[a])
print("\n")

print("3,Reverse: ")
print("Result: \n")
mylist=["mango","is","tasty"]
print("Normal: ",mylist)
mylist.reverse()
print("Reversed: ",mylist)
print("\n")

print("4,Uppercase: ")
text=str(input("Enter your sentence to make it Uppercase: "))
print("Result: \n")
print("The sentence is: ",text.upper())
print("\n")

print("5,Lowercase: ")
text=str(input("Enter your sentence to make it lowercase: "))
print("Result: \n")
print("The sentence is: ",text.lower())
print("\n")

print("6,Length: ")
print("Result: \n")
n1=str(input("Enter your name: "))
print("The length of your name is: ",len(n1))
print("\n")