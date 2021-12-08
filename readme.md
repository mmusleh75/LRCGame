# Left, Right, Center Game
How to Play (here is a video link as well: https://www.youtube.com/watch?v=OxxpTWk3Rx0):
This game has two components: dice and chips. There are 3 dice. Each die has 6 sides: 1 side says ‘left’, 1 says ‘right’, 1 says ‘center’
the remaining 3 sides are blank.

Each player starts with 3 chips. The game ends when all but one player is out of chips (the player with the chips is the winner).

Play starts by rolling the dice. The current player takes the number of dice equal to the number of chips they have, up to 3. If they don’t have chips, they are still in the game but their turn is passed – they can acquire chips as play proceeds.

For each die that indicates LEFT, the player passes that number of chips to the player to the left.

For each die that indicates RIGHT, the player passes that number of chips to the player to the right.

For each die that indicates CENTER, the player passes that number of chips to the center. Once chips are in the center they are out of play.

No action is required for BLANK dice.

When only one player has chips, the player with the chips gets all of the chips from the center and is the winner.

Your program:
* Can accommodate N number of players, ask the user for this number.
* Ask the user to name the players.
* Once the user sets up the names, this program runs automatically without any interaction from the user.
* You will want to manage the players using a list.
* Move chips around via player objects (this is where OOP comes in)
* For each player turn, print the dice roll. Then print status of each player and the center.

~~~~
Roll: R,C,-
Player1 has 3 chips.
Player2 has 2 chips.
Player3 has 2 chips.
Center has 2 chips.
~~~~
 
• FYI – the total number of chips is always the number of players * 3. This is a good way to check your program as it runs.
• When the game is over, print out who the winner is.
