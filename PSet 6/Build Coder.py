'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    out = {}
    for i in string.ascii_uppercase:
        out[i] = chr(((ord(i) + shift - 91) % 26) + 65)
        
    for i in string.ascii_lowercase:
        out[i] = chr(((ord(i) + shift - 123) % 26) + 97)
        
    return out