# Rock Paper Scissors
This is a Python 3 implementation of Rock Paper Scissors which is played in the terminal.

## Pre-Requisites
This app was built using **Pipenv**, so the only pre-requisite is that you have that installed! Pipenv will create a 
virtual environment where it will install all the required packages (including the necessary version of Python) to run 
this app.
* **pip** installation: `pip install --user pipenv`
* **Homebrew / Linuxbrew** installation: `brew install pipenv`

Full Pipenv installation instructions can be found [here](https://docs.pipenv.org/install/#installing-pipenv).

## Setup
1) Clone this project.
2) In your terminal, `cd` to the project root directory (`/python_rps`)
3) You can then run the app in the terminal, or an IDE of your choice that is compatible with Python (e.g. PyCharm, 
   Spyder, IDLE, etc):
    ### Terminal
    * From the project root directory in your terminal,run the following code: 
       ```
       pipenv install
       pipenv shell
       python ./rps/main.py
       ```
      This installs the required packages, creates a virtual environment in which the app can run, and then runs the app.
    ### IDE
    * Run the `main.py` file in your IDE of choice
        * For the game to run properly, please make sure you configure the project to **emulate terminal in output 
          console**. This is required to ensure that player move entry is hidden.
        * For example, in PyCharm, you would configure your run like this:
        ![img.png](assets/pycharm_config_screenshot.png)

## How To Play
Once you have started up the game, a new game session will immediately launch. This game is for 2 players and there is 
the option to play solo or with someone else. If you are playing solo, a CPU player will make its own moves 
automatically.

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

## FAQ
1) **Why is the output displaying weirdly in my Git Bash, with lots of random strings at the beginning?**

    This app has been setup to apply a colour scheme to the console output using an ANSI colour scheme. If you are using 
    a Windows OS and your Git Bash is using the MinTTY terminal, it will not be ANSI compatible. To work around this, 
    you can either:
    * Uninstall then reinstall Git Bash, ensuring you select **Use Windows default console window**
    when configuring the terminal emulator.
    * Run the app in a Python compatible IDE such as PyCharm, making sure it is configured to emulate terminal in the 
      output console (see **Setup** above)
    * Use another terminal which is ANSI compatible, such as `cmd` or `Powershell`.
    * Use a Linux or MacOS system (super simple, right?)
    

2) **This game is crazy fun and super slick. You must have TONNES of Python experience, right?**
    
    That's very kind of you to say, but this is actually my first ever Python app!