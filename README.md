# Rock Paper Scissors
This is a Python 3 implementation of Rock Paper Scissors which is played in the terminal.

## Setup
To run the game:
* Run the `main.py` file in your IDE of choice
    * For the game to run properly, please make sure you configure the project to emulate terminal in output console. 
      This is required to ensure that player move entry is hidden.
    * For example, in PyCharm, you would configure your run like this:
    ![img.png](assets/pycharm_config_screenshot.png)
* Run `<your python executable> .rps/main.py` from the project root directory in the terminal of your choice
    * e.g. `python.exe ./rps/main.py`
    * e.g. `python3 ./rps/main.py`
    
## How To Play
Once you have started up the game, a new game session will immediately launch. This game requires exactly 2 players and 
you will be asked to enter the player names first.

Once players have been set up, each player will need to select their move by entering a number in the terminal. Your
entry will not be displayed so that your opponent will not know what your move is (assuming they're not looking at the
keyboard)!

| Input | Move     |
|:-----:|:--------:|
|   1   | ROCK     |
|   2   | PAPER    |
|   3   | SCISSORS |

Player 1 goes first. Once both players have entered their moves, the game will automatically work out who the winner is.

At the end of each match, you will have 3 options available to you:

| Input | Option                |
|:-----:|:----------------------|
|   s   | View the scoreboard   |
|   p   | Play another match    |
|   q   | Quit the game         |