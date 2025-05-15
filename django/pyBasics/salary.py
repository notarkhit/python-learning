def getTax(salary):
    temp = salary;
    tax = 0

    if salary <= 80000:
        tax += (temp - 50000) * 0.05
    elif salary <= 1100000:
        tax += (80000 - 50000) * 0.05
        tax += (salary - 80000) * 0.1
    elif salary <= 1500000:
        tax += (80000 - 50000) * 0.05
        tax += (80000) * 0.1
        tax += (salary - 1100000) * 0.12
    elif salary <= 2000000:
        tax += (salary - 1500000) * 0.15
    else:
        tax += (salary - 2000000) * 0.3
    return tax;

salary = int(input("Enter Your Salary: "))
tax = getTax(salary)


print(f"Salary: {salary}, tax:{tax}")
