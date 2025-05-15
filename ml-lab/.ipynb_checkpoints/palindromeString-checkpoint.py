def isPalindromeString(str):
    rev = str[::-1]
    if str == rev:
        return True
    else:
        return False

st = input("Enter a string :")

if(isPalindromeString(st)):
    print("Palindrome")
else:
    print("not a Palindrome")

