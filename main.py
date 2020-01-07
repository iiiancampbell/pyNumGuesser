from random import randint

x = 0
def generateNumber(lower, higher):
    if(lower < 0):
        print("lowerBound is below 0 and cannot be used.")
        return
    elif(higher > 0):
        global x
        x = randint(lower, higher)
        return x


msg = "Please enter two numbers (signifying the lower and upper bounds of the number range):"
print(msg)
lowerBound = int(input("First Number: "))
upperBound = int(input("Second Number: "))
while lowerBound > upperBound:
    print("First number is larger than the second number, please retry: ")
    lowerBound = int(input("First Number: "))
    upperBound = int(input("Second Number: "))

x = generateNumber(lowerBound, upperBound)
print(x)
guessCount = 0
userGuess = int(input("Now enter your guess: "))
while userGuess != x:
    if userGuess > x:
        print("Guess lower...")
        guessCount += 1
        userGuess = int(input("Guess count " + str(guessCount) + ": "))
    elif userGuess < x:
        print("Guess higher...")
        guessCount += 1
        userGuess = int(input("Guess count " + str(guessCount) + ": "))
if userGuess == x:
    if guessCount == 1:
        print("You guessed correctly! It Took " + str(guessCount) + " attempt. Good job!")
    else:
        print("You guessed correctly! It Took " + str(guessCount) + " attempts. Good job!")


