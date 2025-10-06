rows = int(input("Enter your no. of rows: "))

def display():
   
    pattern = ""
    for i in range(1, rows + 1):
        pattern += " " * (rows - i) + "*" * (2 * i - 1) + "\n"
    for i in range(rows - 1,0,-1):
        pattern += " " * (rows - i) + "*" * (2 * i - 1) + "\n"
    print(pattern)




display()
