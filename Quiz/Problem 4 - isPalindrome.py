'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def isPalindrome(aString):
    if aString == '':
        return True
    for i in range(len(aString)):
        if aString[i] != aString[len(aString)-((1*i)+1)]:
            return False
    return True
