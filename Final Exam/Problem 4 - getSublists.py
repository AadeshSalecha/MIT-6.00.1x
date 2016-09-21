'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def getSublists(L ,n):
    ans = []
    for i in range((len(L) - n) + 1):
        ans.append(L[i:i+n])
        
    return ans