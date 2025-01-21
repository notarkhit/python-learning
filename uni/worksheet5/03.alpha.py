
char = input("Enter a character: ")

vowels = 'AaEeIiOoUu'

if char in vowels:
    print('vowel dattebayo')
elif char.isalpha():
    print('consonant dattebayo')
else: 
    print('not a dattebayo')
