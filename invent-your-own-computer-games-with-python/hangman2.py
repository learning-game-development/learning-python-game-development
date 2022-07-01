import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===
''', '''
 +---+
 O   |
     |
     |
    ===
''', '''
 +---+
 O   |
 |   |
     |
    ===
''', '''
 +---+
 O   |
/|   |
     |
    ===
''', '''
 +---+
 O   |
/|\  |
     |
    ===
''', '''
 +---+
 O   |
/|\  |
/    |
    ===
''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===
''', '''
 +---+
[O   |
/|\  |
/ \  |
    ===
''', '''
 +---+
[O]  |
/|\  |
/ \  |
    ===
''']

words = {
    'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
    'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    'Animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep kunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
}


def get_random_word(word_dict):
    # This function returns a random string from the passed dictionary of lists of strings and its key.
    # First, randomly select a key from the dictionary:
    word_key = random.choice(list(word_dict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')

    print()

    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters.
    for i in range(len(secretWord)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')

    print()


def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = ''
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = get_random_word(words)
gameIsDone = False

while True:
    print("The secret word is in the set:", secretSet)
    display_board(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = get_guess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            display_board(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if play_again():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = get_random_word(words)
        else:
            break
