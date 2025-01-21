
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1==side2 and side1 == side3:
    print("equilateral")
elif side1==side2 or side2 == side3 or side1 == side3:
    print("isosceles")
else:
    print("scalene")
