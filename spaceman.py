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

def is_word_guessed(secret_word, letter_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letter_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letter_guessed,
        False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    # not in explanation: https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python

    # print(secret_word)
    # print(letter_guessed)
    for letter in secret_word:
        # print(letter)
        if letter not in letter_guessed:
            # print("false")
            return False
    # print("true")
    return True
    # pass

def get_guessed_word(secret_word, letter_guessed):
    '''
    A function that is used to get a string showing the letters
    guessed so far in the secret word and underscores for letters that
    have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letter_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the
        user has guessed correctly, the string should contain the letter at the correct
         position.  For letters in the word that the user has not yet guessed, shown an _
         (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters
    #that have been guessed correctly so far that are saved in letter_guessed and underscores
    #for the letters that have not been guessed yet

    display_word = ""

    for letter in secret_word:
        if letter in letter_guessed:
            display_word += letter
        else:
            display_word += "_"

    return display_word

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

    if guess in secret_word:
        return True
    else:
        return False

    #pass

# play again: https://stackoverflow.com/questions/17897183/python-starting-the-game-again
def play_again():
    while True:
        answer = input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        elif answer.lower() in ('n', 'no'):
            return False
        else:
            print("Not a valid answer!")

def spaceman(secret_word):

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    guesses_left = 7
    guess = ''
    guessed = set()
    letter_guessed = ""
    letters_guessed = []


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

    print(secret_word)

    while guesses_left > 0:
        input_recieved = False
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

        while input_recieved == False:
            guess = input("Enter a letter: ").strip()
            if len(guess) < 1:
                print("You didn't enter anything")
            elif len(guess) > 1:
                print("Please only enter one letter at a time")
            elif guess in letter_guessed:
                print("You already guessed that letter")
            elif not guess.isalpha():
                 print("That's not a letter")
            else:
                input_recieved = True
                letters_guessed.append(guess)    # add letter to array to keep track of user guesses

        letter_guessed += guess

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        # print(guess)
        # print(secret_word)

        if is_guess_in_word(guess, secret_word) == True:
            print("Your guess appears in the word!")
        else:
            print("Sorry, your guess was not in the word, try again")
            guesses_left -= 1

        #TODO: show the guessed word so far
        print("guessed word: " + get_guessed_word(secret_word, letter_guessed))

        #print how many guesses are left
        print("You have " + str(guesses_left) + " incorrect guesses, please enter one letter per round")

        # show letters that have not been guessed yet
        # about sets: https://stackoverflow.com/questions/57840813/how-to-remove-a-character-from-string-after-every-loop-in-a-while-loop
        guessed.add(guess)
        print("These letters haven't been guessed yet: " + ''.join(sorted(alphabet - guessed)))
        print("-------------------------------------")


    #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letter_guessed):
            print("You won!")
            break;
        elif guesses_left < 0:
            print("Sorry you didn't win, try again!")


def main():
    while True:
        spaceman(load_word())
        if not play_again():
            return


if __name__ == '__main__':
    main()
    exit()

main()
