
## Hyperskill - Python - ROCK PAPER SCISSORS 

Stage 1 - Objective

    - Take input from the user;
    - Find an option that wins over the user's option;
    - Output the line: Sorry, but the computer chose <option>.

Stage 2 - Objectives

    - Read user's input that includes the option that users have chosen;
    - Choose a random option;
    - Compare the options and determine the winner;
    - Output one of the lines above, depending on the result of the game.

Stage 3 - Objectives

    - Take input from users;
    - If the input contains !exit, output Bye! and stop the game;
    - If the input is the name of the option, then:
    - Pick a random option
    - Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
        Lose -> Sorry, but the computer chose <option>
        Draw -> There is a draw (<option>)
        Win -> Well done. The computer chose <option> and failed
    - If the input corresponds to anything else, output Invalid input;
    - Repeat it all over again.

Stage 4 - Objectives

    - Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
    - Read input specifying the user's name and output a new line Hello, <name>
    - Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
    - Play the game by the rules defined on the previous stages:
    - Read user's input
    - If the input is !exit, output Bye! and stop the game
    - If the input is the name of the option, then:
    - Pick a random option
    - Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
    - Lose -> Sorry, but the computer chose <option>
    - Draw -> There is a draw (<option>)
    - Win -> Well done. The computer chose <option> and failed
    - For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
    - If the input corresponds to anything else, output Invalid input
    - Play the game again


Stage 5 - Objectives

    - Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following the output!)
    - Read input specifying the user's name and output a new line Hello, <name>
    - Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting the user's score from 0.
    - Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
    - Output a line Okay, let's start
    - Play the game by the rules defined in the previous stages:
        * Read the user's input
        * If the input is !exit, output Bye! and stop the game
        * If the input is the name of the option, then:
          - Pick a random option
          - Output a line with the result of the game in the given format
          - Lose -> Sorry, but the computer chose <option>
          - Draw -> There is a draw (<option>)
          - Win -> Well done. The computer chose <option> and failed
          - For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
        If the input corresponds to anything else, output Invalid input
        Play the game again (with the same options that were defined before the start of the game)

Have fun !
