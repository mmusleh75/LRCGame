import random

class Player():
    def __init__(self, name, marbles):
        self.name = name
        self.marbles = marbles

    def getName(self):
        return self.name

    def getMarbles(self):
        return self.marbles

guessList = ["Odd", "Even"]

def GameOver():
    if player1.getMarbles() > 0 and player2.getMarbles() > 0:
        return False
    else:
        return True

def Roll(playingPlayer, opponentPlayer):
    print(f"{player1.getName()} has {player1.getMarbles()}")
    print(f"{player2.getName()} has {player2.getMarbles()}")

    playerInHand = random.randint(1, playingPlayer.getMarbles())

    opponentPlayerGuess = random.choice(guessList)

    playerHolding = "Odd"
    if playerInHand % 2 == 0:
        playerHolding = "Even"

    print(f"{playingPlayer.getName()} is holding {playerInHand} ({playerHolding}), {opponentPlayer.getName()} guessed ({opponentPlayerGuess})")

    # if the answer is correct
    if opponentPlayerGuess == playerHolding:
        if playingPlayer.getMarbles() < playerInHand:
            print(f"{playingPlayer.getName()} does not have enough, moving {playingPlayer.getMarbles()} from {playingPlayer.getName()} to {opponentPlayer.getName()}")
            opponentPlayer.marbles += playingPlayer.getMarbles()
            playingPlayer.marbles = 0
        else:
            print(f"moving {playerInHand} from {playingPlayer.getName()} to {opponentPlayer.getName()}")
            opponentPlayer.marbles += playerInHand
            playingPlayer.marbles -= playerInHand

    else: # if the answer is wrong
        if opponentPlayer.getMarbles() < playerInHand:
            print(f"{opponentPlayer.getName()} does not have enough, moving {opponentPlayer.getMarbles()} from {opponentPlayer.getName()} to {playingPlayer.getName()}")
            playingPlayer.marbles += opponentPlayer.getMarbles()
            opponentPlayer.marbles = 0
        else:
            print(f"moving {playerInHand} from {opponentPlayer.getName()} to {playingPlayer.getName()}")
            playingPlayer.marbles += playerInHand
            opponentPlayer.marbles -= playerInHand

if __name__ == "__main__":

    player1 = Player("John", 5)
    player2 = Player("Steve", 5)

    # the values for the two players can be replaced with input()

    while True:

        if player1.getMarbles() > 0:
            Roll(player1, player2)
            if GameOver():
                break

        if player2.getMarbles() > 0:
            Roll(player2, player1)
            if GameOver():
                break

    print("--------------------------------------------")
    if player1.getMarbles() > 0:
        print(f"{player1.getName()} has {player1.getMarbles()} and is the winner")
    else:
        print(f"{player2.getName()} has {player2.getMarbles()} and is the winner")
