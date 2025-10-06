def interest():
    choice = input("Which interest would you like to calculate? (simple/compound): ").lower()
    print("\n")

    P=int(input("Enter your principle value:₹ "))
    R=float(input("Enter Your rate of interest:% "))
    T=float(input("Enter your time in years: "))
    print("\n")

    if choice == "simple":
           SI=(P*R*T)/100
           print("The simple interest would be:₹ ",SI)
           total=P+SI
           print("The total value will be:₹ ",total)

    elif choice == "compound":
            N=int(input("Enter the number of times interest compounded per year: "))
            print("\n")
            A = P * (1 + R / (100 * N)) ** (N * T)
            CI = A - P
            print("The Compound interest would be:₹ ",CI)
            total=P+CI
            print("The total value will be:₹ ",A)

    else:
          print("Invalid choice. Please choose either 'simple' or 'compound'.")

          
interest()
