num=int(input("Enter your number:  "))   

print("\n")

P=list(map(lambda x: 2**x,range(num)))

for power in P:
    print(power)