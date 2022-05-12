from os import system
from keyboard import is_pressed

while True:
    system("cls")
    theWord = input("The secret word: ")
    system("cls")

    #Initializes the needed variables
    wonOrNot = False
    guessedLetters = []
    #Game's loop
    for chance in range(int(len(theWord)*1.5)):
        #Gets what user has guessed
        userGuess = input("Your guess: ").lower()
        #Defines letter index for putting the thing into a list
        letterIndex = 0
        #Checks if any of the is in the word
        for letter in theWord:
            if letter.lower() == userGuess:
                guessedLetters.insert(letterIndex, userGuess)
            letterIndex += 1
        print(guessedLetters)
        #Converts the guessed letters list to string
        strGuessedLetters = ""
        for letter in guessedLetters:
            strGuessedLetters += str(letter)
        #Checks if you guessed the hole word
        if strGuessedLetters == theWord.lower():
            wonOrNot = True
            #Tells the player status if the player lost
            if wonOrNot:
                print("You won!")  
            break
    #Tells the player status if the player won
    if wonOrNot == False:
        print("Game over!")

    print("\nPlay again? press s\nToo tired? press e")
    
    #Checks the keys so it figures out if the player wants to play again
    while True:
        if is_pressed("s"):
            break
        if is_pressed("e"):
            exit()