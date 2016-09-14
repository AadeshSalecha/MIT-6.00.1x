'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a = 0
    # FILL IN YOUR CODE HERE...
    lower = "abcdefghijklmnopqrstuvwxyz"
    for i in lettersGuessed:
        a = lower.find(i)
        lower = lower[:a] + lower[a+1:]
        
    return lower