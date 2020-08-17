HEADER = '''

                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \___________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

 _           _   _   _           _     _       
| |         | | | | | |         | |   (_)      
| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                        | |    
                                        |_|    

'''

GAMEPLAY = '''
    Battleship
    ----------

    Goal
    ----

    Battleship is a war-themed board game for two players in which the opponents
    try to guess the location of their opponent's warships and sink them shoting it.

    * Players: 2

    Setting up the Game
    -------------------

    Each player receives a game board and 5 ships of varying lengths.
    Each ship has holes where the "hit" pegs are inserted and a supply
    of hit and miss markers (white and red pegs).

    The five ships are:

    * Carrier, which has 5 holes
    * Battleship, which has 4 holes
    * Cruiser, which has 3 holes
    * Submarine, which has 3 holes
    * Destroyer, which has 2 holes

    Each ship must be placed horizontally or vertically
    across grid spaces—not diagonally —and the ships can't hang off the grid.
    Ships can touch each other, but they can't occupy the same grid space.
    You cannot change the position of the ships after the game begins.

    There no rules about who starts first.


    Basic Gameplay
    --------------

    Players take turns firing shots (by calling out a grid coordinate)
    to attempt to hit the opponent's enemy ships.

    On your turn, call out a letter and a number that identifies a row and column on your target grid.
    Your opponent checks that coordinate on their ocean grid and responds "miss" if there is no ship there, or "hit" if
    you have correctly guessed a space that is occupied by a ship.

    Mark each of your shots or attempts to fire on the enemy using your target grid (upper part of the board)
    by using white pegs to document your misses and red pegs to register your hits.
    As the game proceeds, the red pegs will gradually identify the size and location of your opponent's ships.

    When it is your opponent's turn to fire shots at you, each time one of your ships receives a hit, put a
    red peg into the hole on the ship corresponding to the grid space. When one of your ships has every slot filled with
    red pegs, you must announce to your opponent when your ship is sunk. In classic play,
    the phrase is "You sunk my battleship!"

    The first player to sink all five of their opponent's ships wins the game.

'''

INSTRUCTIONS = '''

    Battleship CLI
    --------------

    INSTRUCTIONS
    ------------

    1. First, write the players name using the 'p1' and 'p2' commands:

    battleship> p1 <Name Player 1>		// e.g. p1 Cristian

    battleship> p2 <Name Player 2>		// e.g. p2 Emmanuel

    2. Second, starts the game using the 'start' command. This will initialize the boards for each player.

    battleship> start

    3. Then, each player have to place their ships using the 'place_ship_p1' and 'place_ship_p2':

    battleship> place_ship_p1 <row> <col> <ship> <aligment>		// e.g. place_ship_p1 A 1 carrier H

    battleship> place_ship_p2 <row> <col> <ship> <aligment>		// e.g. place_ship_p2 A 1 carrier H


    Tips and Notes:

    - Each board support a max. of 5 ships.
    - Run 'ls ships' or 'ls s' to see all available ships.
    - Run 'ls aligments' or 'ls a' to see all available aligments.
    - Run 'ls rows' or 'ls r' to see all available rows.
    - Run 'ls cols' or 'ls c' to see all available columns.

    4. Then, run 'play' to start shootig!:

    battleship> play


    5. Finally, each player can start shooting at each other:

    battleship> shoot_p1 <row> <col>		// e.g. shoot_p1 A 1

    battleship> shoot_p2 <row> <col>		// e.g. shoot_p2 A 1

    Tips:
    - Run 'help shoot_p1' or 'help shoot_p2' to see the usage.

'''
