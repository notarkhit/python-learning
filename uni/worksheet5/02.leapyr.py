year = int(input('Enter a year'))

if (year%4)!=0:
    print(False)

elif (year%100)!=0:
    print(True)
else:
    print(True)
