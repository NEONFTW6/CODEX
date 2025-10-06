num = float(input("Enter your number: "))

inte=int(num)
binary=bin(inte)
octal=oct(inte)
hexa=hex(inte)
print("\n")

print(f"binary number of {num}:",binary[2:])
print(f"octal number of {num}:",octal[2:])
print(f"hex number of {num}:",hexa[2:])