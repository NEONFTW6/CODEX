x =int(input("Enter the number for the required multiplication table: "))
print("\n")

print(f"The multiplication table of {x} is: ")
for i in range(1,21):
    print(f"{x}x{i} = {x*i}")

 