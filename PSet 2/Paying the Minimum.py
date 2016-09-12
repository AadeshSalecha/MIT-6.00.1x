'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
month = 0
monthlyInterestRate = annualInterestRate/12.0
a = 0

while month <= 11:
    month = month + 1
    mp = round(monthlyPaymentRate * balance , 2)
    mub = balance - mp
    balance = round(mub + monthlyInterestRate * mub, 2)
    a = a + mp
    
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(mp)
    print 'Remaining balance ' + str(balance)
    
    if month == 12:
        print 'Total paid: ' + str(a)
        print 'Remaining balance: ' + str(balance)
