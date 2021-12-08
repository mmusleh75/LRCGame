import random
# players [p1,p2,p3]
# players [0 ,1 ,2]

class Player:
    # Constructor. Define and initialize attributes of the class using
    # self.attributename
    def __init__(self, name):
        self.name = name
        self.chips = 3

    # Create accessors for each attribute, e.g. getName()
    def getName(self):
        return self.name

    def getNumChips(self):
        return self.chips

    # Define two functions that (1)add and (2)remove chips from the player.
    # Functions should be as generic as possible, instead of always removing one
    # chip, consider the option of have the number of chips to add or remove
    # as a parameter given to the function.
    def addChips(self, numChips):
        self.chips = self.chips + numChips

    def removeChips(self, numChips):
        self.chips = self.chips - numChips
        if self.chips < 0:
            self.chips = 0

    # create an str function that will print the attributes. Remember this
    # function has to be named __str__ and it returns the completed string
    # as it would appear in a print statement. Because you will be printing
    # the attributes, build a string using those attributes.
    def __str__(self):
        return f"{self.name} has {self.chips} chips."


# notOver is a function that determines if the game is over by looking through
# the chips held by each player. If all but one player has zero chips, the game
# is over.
# @param players a list of players in the game.
# returns True if more than one player has chips.
# returns False if only one player has chips.
def notOver(players):
    playersInGame = 0

    for player in players:
        if player.getNumChips() > 0:
            playersInGame += 1

    if playersInGame > 1:
        return True

    return False

# rollDice function rolls 3 dice if the player has 3 or more chips, otherwise
# rolls the number of dice equal to the number of chips the current player has.
# @param numChips the number of chips that the player has.
# @param dieResults a list containing the roll of 3 dice. 'L' = Left (1 in 6
# chance), 'R' = Right (1 in 6 chance), 'C' = Center (1 in 6 chance),
# '-' = Hold (3 in 6 chance)
# returns the number of dice rolled, dieResults is a list so it is automatically
# returned via the call.
def rollDice(numChips, dieResults):
    numDice = numChips

    if numChips >= 3:
        numDice = 3

    dieList = ['R','L','C','.','.','.']

    die1 = random.choice(dieList)
    die2 = random.choice(dieList)
    die3 = random.choice(dieList)

    dieResults.append(die1)
    dieResults.append(die2)
    dieResults.append(die3)

    return numDice


# winner determines which player is the winner of the game - the player with chips.
# once determined, the center chips are added to the players chips and a message
# is printed to the screen.
# @param players - a list of players
# @centerChips - number of chips in the center
def winner(players, centerChips):
    # Here is a print statement that you may use if you so choose.
    for player in players:
        if player.getNumChips() > 0:
            print(f'The winner is {player.getName()} with {player.getNumChips()+centerChips} chips.')


# main drives the game.
def main():
    # create an empty list of players
    players = []

    # ask the user how many players are in the game.
    numberOfPlayer = 3 #input("Number of players?")
    for i in range(int(numberOfPlayer)):
        # then ask for player names as you add each new player to the list
        playerName = f"player-{i}" #input("player "+str(i)+" name?")
        playerObject = Player(playerName)
        players.append(playerObject)

    # create and initialize variables
    centerChips = 0
    dieResults = []

    # set the index for the starting player
    currPlayer = 0
    while (notOver(players)):

        # if the current player has chips, they get a turn.
        # print which player is taking a turn and roll the dice using the function.

        for player in players:
            if player.getNumChips() > 0:
                print(f"+ {player.getName()} is rolling dice")
                print()
                numDice = rollDice(player.getNumChips(), dieResults)

            # one at a time, look at each die and take the appropriate action:
            # move a chip to the left, right, center or hold on to the chip.
            # this is a good time to use a mod function to index the player to
            # the left and the right.

                # creates comma delimeted list
                print("Roll: ", ",".join(dieResults))

                RightDieCnt = dieResults.count("R")
                LeftDieCnt = dieResults.count("L")
                CenterDieCnt = dieResults.count("C")

                currPlayer = players.index(player)

                if currPlayer == 0:
                    rightPlayer = currPlayer+1
                    leftPlayer = len(players)-1
                elif currPlayer == len(players) - 1:
                    rightPlayer = 0
                    leftPlayer = len(players)-2
                else:
                    rightPlayer = currPlayer + 1
                    leftPlayer = currPlayer - 1

                lostChips = RightDieCnt + LeftDieCnt + CenterDieCnt

                players[currPlayer].removeChips(lostChips)
                players[rightPlayer].addChips(RightDieCnt)
                players[leftPlayer].addChips(LeftDieCnt)
                centerChips = centerChips + CenterDieCnt

                # print the chip standings (the number of chips each player has)
                print(f'Chip Standing')
                for i in range(len(players)):
                    print(players[i])
                print()
                print(f'{centerChips} in the center.')
                print()

                dieResults = []

    # set the current player to the next player (mod is a good way to do this)

    # once the game is over, determine the winner using the winner function
    winner(players, centerChips)

main()
