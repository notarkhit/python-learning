def isPalindrome(num):
    temp = num
    reverse = 0

    while temp>0:
        reverse = (reverse*10) + (temp%10)
        temp = temp/10

    if num == reverse:
        return True
    else:
        return False

print(isPalindrome(121))
