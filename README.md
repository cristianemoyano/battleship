# Battleship CLI


	Battleship CLI
    --------------

    $ python3 game/cli.py

    INSTRUCTIONS
    ------------

    1. First, write the players name using the 'p1' and 'p2' commands:

    battleship> p1 <Name Player 1>      // e.g. p1 Cristian

    battleship> p2 <Name Player 2>      // e.g. p2 Emmanuel

    2. Second, starts the game using the 'start' command. This will initialize the boards for each player.

    battleship> start

    3. Then, each player have to place their ships using the 'place_ship_p1' and 'place_ship_p2':

    battleship> place_ship_p1 <row> <col> <ship> <aligment>     // e.g. place_ship_p1 A 1 carrier H

    battleship> place_ship_p2 <row> <col> <ship> <aligment>     // e.g. place_ship_p2 A 1 carrier H


    Tips and Notes:

    - Each board support a max. of 5 ships.
    - Run 'ls ships' or 'ls s' to see all available ships.
    - Run 'ls aligments' or 'ls a' to see all available aligments.
    - Run 'ls rows' or 'ls r' to see all available rows.
    - Run 'ls cols' or 'ls c' to see all available columns.

    4. Then, run 'play' to start shootig!:

    battleship> play


    5. Finally, each player can start shooting at each other (Always start playing Player 1):

    battleship> shoot <row> <col>       // e.g. shoot A 1


    Tips:
    - Run 'help shoot' to see the usage.


## Tests

```bash
python3 -m unittest test_main.py
```