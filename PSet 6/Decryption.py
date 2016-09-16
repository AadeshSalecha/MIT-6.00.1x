'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    return applyShift(getStoryString(), findBestShift(loadWords(),getStoryString()))
