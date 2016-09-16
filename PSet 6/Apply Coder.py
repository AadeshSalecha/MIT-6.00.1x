'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    result = ''
    for i in text:
        if i.isalpha():
            result = result + coder[i]
        else:
            result = result + i
        
    return result