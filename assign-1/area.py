print("Choose your shape from the following: ")

print("\n")

print("1,Triangle")
print("2,Square")
print("3,Rectangle")
print("4,Circle")
print("5,Cube")

print("\n")

shape=input("Enter number accordig to your shape: ")

print("\n")

if shape == '1':
     base =float(input("Enter your value for base of triangle: "))
     height =float(input("Enter your value for height of triangle: "))
     area = 0.5 * base * height
     print(f"The area of triangle is: {area}")

elif shape == '2':
     side =float(input("Enter your value for side of square: "))     
     area = side ** 2
     print(f"The area of square is: {area}")
    
elif shape =='3':
     length =float(input("Enter your value for height of rectangle: "))
     width =float(input("Enter your value for width of rectangle: "))
     area = width * length
     print(f"The area of rectangle is: {area}")

elif shape =='4':
     radius =float(input("Enter your value for radius of circle: "))
     area =3.14 * radius**2
     print(f"The area of circle is: {area}")

elif shape =='5':
     side =float(input("Enter your value for side of cube: "))
     surfacearea=6 * side**2
     print(f"The surfacearea of cube is: {surfacearea}")

else:
     print("Invalid choice!,Please try again.")

