x = int(input("Enter your 1st num: " ))
y = int(input("Enter your 2nd num: "))

print(f"The prime intervals between {x} and {y} are: ")

for i in range(x+1,y):
    if i>1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            print(i)