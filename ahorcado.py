import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colores':'rojo naranja amarillo verde azul indigo violeta blanco negro marron'.split(),
'Formas':'cuadrado triangulo rectangulo circulo rombo pentagono hexagono octogono'.split(),
'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana mango fresa tomate'.split(),
'Animales':'murcielago oso castor gato puma ciervo perro burro pato aguila pez rana cabra leon lagartija mono raton nutria buho panda python conejo rata tiburon oveja tigre pavo tortuga comadreja ballena lobo cebra'.split()}

def getRandomWord(wordDict):
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.'''
    
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('LETRAS PERDIDAS:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Ingrese una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor ingrese solo una letra.')
        elif guess in alreadyGuessed:
            print('Ya ha ingresado esa letra. Ingrese otra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Ingrese una letra.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Quiere jugar de nuevo?(si o no)')
    return input().lower().startswith('s')


print('A H O R C A D O')

difficulty = 'X'
while difficulty not in 'FMD':
  print('Ingrese dificultad: F - Facil, M - Medio, D - Dificil')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'D':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('La palabra secreta está en.... ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Si! La palabra secreta es "' + secretWord + '"! GANASTE!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Te quedaste sin oportunidades!\nDespués de ' + str(len(missedLetters)) + ' letras incorrectas ' + str(len(correctLetters)) + ' letras correctas, la palabra era "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break