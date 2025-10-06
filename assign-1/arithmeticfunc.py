def arithmetic():
    x= int(input("Please enter the value of x: "))
    y= int(input("Please enter the value of y: "))
   
    print("\n")
    if x and y > 0:
    
     print("The add of the equation is: ", x+y)
     print("The sub of the equation is ", x-y)
     print("The multi of the equation is", x*y)
     print("The divi of the equation is ", x/y)

    elif x and y == 0:
       print("Enter a positive value")

    else:
       print("Enter a positive value")

arithmetic()