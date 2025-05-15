def isPalindrome(num):
    temp = num
    rev = 0;
    while temp !=0 :
        rev = (rev * 10) + (temp%10)
        temp /= 10;
    print(rev)
    return (num == rev)

num = int(input("Enter a number: "));

print(isPalindrome(num))


