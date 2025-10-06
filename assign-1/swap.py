def swap(a, b):

 return b, a

x =int(input("Enter your number: "))
y =int(input("Enter your number: "))
print("\n")

print("Before swapping:")
print("x =", x)
print("y =", y)

x, y = swap(x, y)

print("\nAfter swapping:")
print("x =", x)
print("y =", y)
