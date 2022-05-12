from os import system

theWord = input("The secret word: ")
system("cls")

guessedLetters = []
for chance in range(5):
    #Gets what user has guessed
    userGuess = input("Your guess: ").lower()
    #defines letter index for putting the thing into a list
    letterIndex = 0
    #checks if any of the is in the word
    for letter in theWord:
        if letter.lower() == userGuess:
            guessedLetters.insert(letterIndex, userGuess)
        letterIndex += 1
    print(guessedLetters)
    #converts the guessed letters list to string
    strGuessedLetters = ""
    for letter in guessedLetters:
        strGuessedLetters += str(letter)
    #checks if you guessed the hole word
    if strGuessedLetters == theWord.lower():
        print("You won!")
        exit()
print("Game over!")