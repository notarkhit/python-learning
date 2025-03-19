def factorial (number):
    fact = 1
    for x in range(1,number):
        fact *= x
    return fact

num = input("Enter number")
print(f"{num}!={factorial(num)}")
