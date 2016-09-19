'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    a =[]
    for item in aList:
        if type(item) == list:
            a = flatten1(a, item)
        else:
            a.append(item)
            
    for item in aList:
        if type(item) == list:
            return flatten(a)
            
    return a
  
def flatten1(aList, item):
    a = []
    for i in aList:
        a.append(i)
        
    for i in item:
        a.append(i)
        
    return a
  