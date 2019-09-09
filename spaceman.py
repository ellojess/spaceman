import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use
    as the secret word from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    word_list = words_list[0].split(' ')
    secret_word = random.choice(word_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    # not in explanation: https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python


    for letter in secret_word:
        if letter not in lettersGuessed:
            return False
        else:
            return True
    # pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters
    guessed so far in the secret word and underscores for letters that
    have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the
        user has guessed correctly, the string should contain the letter at the correct
         position.  For letters in the word that the user has not yet guessed, shown an _
         (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters
    #that have been guessed correctly so far that are saved in letters_guessed and underscores
    #for the letters that have not been guessed yet

    display_word = " "

    for letter in secret_word:
        if letter in letters_guessed:
            display_word += letter
        else:
            display_word += "_"


    # pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    for guess in secret_word:
        return True
    else:
        return False

    #pass


def spaceman(secret_word):

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    guesses_left = 7
    guess = ''
    guessed = set()
    letters_guessed = [ ]
    revealed_word = False

    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec

    print("Welcome to Spaceman!")

    print(f"The secret word contains: {len(secret_word)} letters")

    print("You have " + str(guesses_left) + " incorrect guesses, please enter one letter per round")

    print("-------------------------------------")

    while guesses_left >= 0:
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
        if secret_word != get_guessed_word(secret_word, letters_guessed):
            guess = input("Enter a letter: ")

        if len(guess) < 1:
            print("You didn't enter anything")
            print("-------------------------------------")
        elif len(guess) > 1:
            print("Please only enter one letter at a time")
            print("-------------------------------------")
        elif guess in letters_guessed:
            print("You already guessed that letter")
            print("-------------------------------------")

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("Your guess appears in the word!")
        elif not is_guess_in_word(guess, secret_word):
            guesses_left -= 1
            print("Sorry, your guess was not in the word, try again")
            print("-------------------------------------")

    #TODO: show the guessed word so far

            print(get_guessed_word(secret_word, letters_guessed))

    # show letters that have not been guessed yet
        guessed.add(guess)
        print("These letters haven't been guessed yet: " + ''.join(sorted(alphabet - guessed)))
        print("-------------------------------------")


    #TODO: check if the game has been won or lost
        if revealed_word == True:
            print("You won!")
        elif guesses_left == 0:
            print("Sorry you didn't win, try again!")




#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
