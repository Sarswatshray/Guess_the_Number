import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0
try:
    while(userGuess != randNumber):
        userGuess = int(input("Enter your guess: "))
        guesses += 1
        if(userGuess==randNumber):
            print("You guessed it right!")
        else:
            if(userGuess>randNumber):
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a larger number")

except Exception as e:
    print(f"Your input resulted in an error ({e})")

print(f"You guessed the number in {guesses} guesses")