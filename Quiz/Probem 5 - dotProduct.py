'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def dotProduct(listA, listB):
    zigma = 0
    for i in range(len(listA)):
        zigma += listA[i] * listB[i]
        
    return zigma