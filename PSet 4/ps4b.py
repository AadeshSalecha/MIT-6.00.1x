'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        if isValidWord(i, hand, wordList):
            # Find out how much making that word is worth
            if getWordScore(i, n) > max_score:
            # If the score for that word is higher than your best score
                max_score = getWordScore(i, n)
                best_word = i[:]


    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total_score = 0
    # As long as there are still letters left in the hand:
    word = ''
    while (calculateHandlen(hand) > 0):
        # Display the hand
        a = ''
        for i in hand.keys():
            a = a + ' ' + i
        print 'Current Hand: ', a
        
        word = compChooseWord(hand, wordList, n)
        if (word == None):
            break
        total_score += getWordScore(word,n)
        print "\"" + word + "\"" + ' earned ' , getWordScore(word,n) , ' points. Total: ' , total_score , ' points'
        print
        hand = updateHand(hand, word)
          
    print 'Total score: ', total_score , '.'

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand = 0
    prev_hand = 0
    while(True):
        inpu = 0
        while not(inpu == 'n' or inpu == 'r' or inpu == 'e'):
            print 'Enter n to deal a new hand, r to replay the last hand, or e to end game: ',
            inpu = str(raw_input())
            if not(inpu == 'n' or inpu == 'r' or inpu == 'e'):
                print 'Invalid command.'
            print
            
        if (inpu == 'e'):
            break
        elif (inpu == 'r'):
            if (prev_hand == 0):
                print 'You have not played a hand yet. Please play a new hand first!'
                print
            else:
                inpu2 = 0
                while not(inpu2 == 'c' or inpu2 == 'u'):
                    print 'Enter u to have yourself play, c to have the computer play: ',
                    inpu2 = str(raw_input())
                    if not(inpu2 == 'c' or inpu2 == 'u'):
                        print 'Invalid command.'
                    print
                
                if (inpu2 == 'u'):
                    hand = prev_hand
                    prev_hand = hand
                    playHand(hand,wordList,HAND_SIZE)
                    print
                elif (inpu2 == 'c'):
                    hand = prev_hand
                    prev_hand = hand
                    compPlayHand(hand, wordList, HAND_SIZE)
                    print
        
        elif (inpu == 'n'):
            inpu1 = 0
            while not(inpu1 == 'c' or inpu1 == 'u'):
                print 'Enter u to have yourself play, c to have the computer play: ',
                inpu1 = str(raw_input())
                if not(inpu1 == 'c' or inpu1 == 'u'):
                    print 'Invalid command.'
                print
                                            
            if (inpu1 == 'u'):
                hand =  dealHand(HAND_SIZE)
                prev_hand = hand
                playHand(hand,wordList,HAND_SIZE)
                print
            elif (inpu1 == 'c'):
                hand =  dealHand(HAND_SIZE)
                prev_hand = hand
                compPlayHand(hand, wordList, HAND_SIZE)
                print
            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


