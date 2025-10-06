def calc():
 startnum=int(input("Enter your number: "))
 endnum=int(input("Enter your number:"))

 print("\n")

 for i in range(startnum,endnum):
    if i % 2 == 0:
        print(i)
calc()