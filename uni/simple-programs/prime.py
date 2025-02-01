def isPrimeNumber(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

numberToCheck = int(input("Enter a number: "))
if isPrimeNumber(numberToCheck):
    print(f"{numberToCheck} is a prime number.")
else:
    print(f"{numberToCheck} is not a prime number.")

