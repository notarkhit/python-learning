age = int(input('Enter voter age: '))

if age < 0:
    print('unborn')
elif age > 100:
    print('LMAO ded')
elif age < 13:
    print('Child')
elif age < 20:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('senior')


