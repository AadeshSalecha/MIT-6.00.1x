'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    words_got = {}
    
    for i in range(26):
        words = 0
        decrypted = applyCoder(text, buildCoder(i))
        for j in decrypted.split():
            if isWord(wordList, j):
                words += 1
        words_got[i] = words
        
    return max(words_got.iterkeys(), key=lambda k: words_got[k])
    
    
    
    
