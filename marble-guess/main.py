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

def Play(playingBot, opponentBot):
    print(f"{bot1.getName()} has {bot1.getMarbles()}")
    print(f"{bot2.getName()} has {bot2.getMarbles()}")

    playingBotHolds = random.randint(1, playingBot.getMarbles())
    opponentBotGuess = random.choice(guessList)

    playingBotHas = "Odd"
    if playingBotHolds % 2 == 0:
        playingBotHas = "Even"

    print(f"{playingBot.getName()} is holding {playingBotHolds} ({playingBotHas}), {opponentBot.getName()} guessed ({opponentBotGuess})")

    # if the answer is correct
    if opponentBotGuess == playingBotHas:
        if playingBot.getMarbles() < playingBotHolds:
            print(f"{playingBot.getName()} does not have enough, moving {playingBot.getMarbles()} from {playingBot.getName()} to {opponentBot.getName()}")
            opponentBot.marbles += playingBot.getMarbles()
            playingBot.marbles = 0
        else:
            print(f"moving {playingBotHolds} from {playingBot.getName()} to {opponentBot.getName()}")
            opponentBot.marbles += playingBotHolds
            playingBot.marbles -= playingBotHolds

    else: # if the answer is wrong
        if opponentBot.getMarbles() < playingBotHolds:
            print(f"{opponentBot.getName()} does not have enough, moving {opponentBot.getMarbles()} from {opponentBot.getName()} to {playingBot.getName()}")
            playingBot.marbles += opponentBot.getMarbles()
            opponentBot.marbles = 0
        else:
            print(f"moving {playingBotHolds} from {opponentBot.getName()} to {playingBot.getName()}")
            playingBot.marbles += playingBotHolds
            opponentBot.marbles -= playingBotHolds

if __name__ == "__main__":

    bot1 = Player("John", 50)
    bot2 = Player("Steve", 50)

    # the values for the two players can be replaced with input()

    rotation = 0
    while True:

        if bot1.getMarbles() > 0:
            Play(bot1, bot2)
            rotation += 1
            if bot1.getMarbles() == 0:
                break

        if bot2.getMarbles() > 0:
            Play(bot2, bot1)
            rotation += 1
            if bot2.getMarbles() == 0:
                break

    print("--------------------------------------------")
    print(f"Bots played for {rotation} time(s) and the winner is")
    if bot1.getMarbles() > 0:
        print(f"{bot1.getName()} with {bot1.getMarbles()} marbles.")
    else:
        print(f"{bot2.getName()} with {bot2.getMarbles()} marbles.")
