x=int(input("Enter your starting number: "))
y=int(input("Enter your ending number: "))
z=int(input("Enter your divisor: "))

print("\n")

print(f"The number divisble by {z} between {x} and {y} are: ")
print("\n")

for i in range(x,y+1):
    if i%z==0:
        print(i)