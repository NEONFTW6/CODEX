def maxmin():
    
    N1=int(input("Enter your first number: "))
    N2=int(input("Enter your second number: "))
    N3=int(input("Enter your third number: "))

    if( N1 > N2 and N1 > N3):
      print("The first Number is max")

    elif( N2 > N1 and N2 > N3):
      print("The second number is max")

    else:
      print("The third number is max")

    if( N1 < N2 and N1 < N3):
      print("The first Number is min")

    elif( N2 < N1 and N2 < N3):
      print("The second number is min")

    else:
      print("The third number is min")

maxmin()