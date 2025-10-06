startnum=int(input("Enter your number: "))
endnum=int(input("Enter your number:"))

print("\n")

print("Even number: ")
for i in range(startnum,endnum):
    if i % 2 == 0:
        print(i)

print("Odd number: ")
for i in range(startnum,endnum):
    if i % 2 == 1:
        print(i)