# Rock Paper Scissors
This is a Python 3 implementation of Rock Paper Scissors which is played in the terminal.

## Setup
To run the game:
* Run the `main.py` file in your IDE of choice
* Run `<your python executable> .rps/main.py` from the project root directory in the terminal of your choice
    * e.g. `python.exe ./rps/main.py`
    * e.g. `python3 ./rps/main.py`
    
## How To Play
Once you have started up the game, a new game session will immediately launch. This game requires exactly 2 players and 
you will be asked to enter the player names first.

Once players have been set-up, each player will need to select their move by entering a number in the terminal, where:

| Input |   Move   |
|:-----:|:--------:|
|   1   |   ROCK   |
|   2   |  PAPER   |
|   3   | SCISSORS |

Player 1 goes first. Once both players have entered their moves, the game will automatically work out who the winner is.

At the end of each match, you will have 3 options available to you:

| Input |        Option         |
|:-----:|:----------------------|
|   s   | View the scoreboard   |
|   p   | Play another match    |
|   q   | Quit the game         |