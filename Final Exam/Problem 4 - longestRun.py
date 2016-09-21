'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''

def longestRun(L):
    s = L
    curString = 1
    longest =0

    for i in range(0, len(s) - 1):
        if s[i] <= s[i + 1]:
            curString += 1
            if curString > longest:
                longest = curString       
        else:
            curString = 1

    if longest != 0:
        return longest
    else:
        return 1