
voterAge = int(input('Enter voter age: '))

if voterAge > 17 :
    print('Eligible to vote')
elif voterAge==0:
    print('Voter not born yet!!')
else :
    print('Ineligible for voting')
