
number = int(input('Enter a number: '))

if not number:
    print("zero")
    exit(1)

if not number%2:
    print('Even');
else:
    print('odd');

