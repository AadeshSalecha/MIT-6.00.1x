'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balance_cpy = balance
month = 1
monthlyInterestRate = annualInterestRate/12.0
a = 0
mp = 10

while month < 13:
    mub = balance - mp
    balance = round(mub + monthlyInterestRate * mub, 2)
    
    if (month == 12):
            if balance <= 0.00:
                print "The Lowest amount is:" + str(mp)
            else:
                mp = mp + 10
                balance = balance_cpy
                month = 0
    month += 1
    
print 'Remaining balance: ' + str(balance)
