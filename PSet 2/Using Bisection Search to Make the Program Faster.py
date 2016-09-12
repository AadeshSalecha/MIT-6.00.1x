'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
balance = 320000
balance_cpy =  balance

annualInterestRate = 0.2
month = 0
monthlyInterestRate = annualInterestRate/12.0
a = 0

lower = round(balance / 12.00, 2)
upper = balance
mp = round(lower + upper / 2.0,2)

while month <= 11:
    month = month + 1
    mub = balance - mp
    balance = round(mub + monthlyInterestRate * mub, 2)
    a = a + mp
        
    if month == 12:
        if balance > 0.1:
            lower = mp
            mp = (lower + upper) / 2
            balance = balance_cpy
            month = 0
        if balance < -0.1:
            upper = mp
            mp = (lower + upper) / 2
            balance = balance_cpy
            month = 0

mp = round(mp, 2)
print "Lowest Payment: " + str(mp)