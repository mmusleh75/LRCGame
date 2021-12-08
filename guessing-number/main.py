import random


def guessNumber():
    correctAnswer = False
    lowRange=1
    highRange=100

    guessCount = 0
    while not correctAnswer:
        print(f"range is {lowRange} - {highRange}")
        computerGuess = random.randint(lowRange,highRange)
        response = input(f"Is {computerGuess} the correct number? (H|L|M)")
        if response.upper() == "M":
            correctAnswer = True
        elif response.upper() == "H":
            lowRange = computerGuess + 1
        elif response.upper() == "L":
            highRange = computerGuess - 1
        else:
            print("Invalid response, response with H: Higher, L:Lower or M: Match")

        guessCount += 1

    print(f"It took the computer {guessCount} tries to get the number!")

if __name__ == "__main__":
    guessNumber()
