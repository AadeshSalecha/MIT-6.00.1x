'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ', len(secretWord), 'letters long.'
    print '-------------'
    
    guesses = 8
    letters_guessed = []
    
    while(guesses > 0):
        if (isWordGuessed(secretWord, letters_guessed)):
            print 'Congratulations, you won!'
            break
            
        print 'You have ',guesses, 'guesses left.'
	print 'Available letters: ', getAvailableLetters(letters_guessed)
	print 'Please guess a letter:', 
	letter = str(raw_input())
        
        if (letter in letters_guessed):
            print 'Oops! You\'ve already guessed that letter: ',
            print getGuessedWord(secretWord, letters_guessed)
            print '-------------'
        elif (letter not in letters_guessed):
            if letter in secretWord:
                letters_guessed.append(letter)
                print 'Good guess: ',
                print getGuessedWord(secretWord, letters_guessed)
                print '-------------'
            else:
                guesses -= 1
                letters_guessed.append(letter)
                print 'Oops! That letter is not in my word:',
                print getGuessedWord(secretWord, letters_guessed)
                print '-------------'
                
    if (guesses == 0):
        print 'Sorry, you ran out of guesses. The word was',secretWord,'.'
        
    return