def calculateFactorial(number):
    factorialResult = 1
    for i in range(2, number + 1):
        factorialResult *= i
    return factorialResult

factorialNumber = int(input("Enter a number: "))
print(f"Factorial of {factorialNumber} is {calculateFactorial(factorialNumber)}")

