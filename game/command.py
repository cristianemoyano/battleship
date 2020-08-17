from cmd import Cmd

from board import GameBoard
from constants import (
    HEADER,
    GAMEPLAY,
    INSTRUCTIONS,
)
from main import Game
from player import Player
from ship import (
    Ship,
    ShipPosition,
)


class BattleshipCLI(Cmd):
    prompt = 'battleship> '
    intro = "{} \n Welcome to Battleship CLI! Type ? to list commands \n ".format(HEADER)

    ALL_SHIPS = list(Ship.get_ship_map().keys())
    ALL_ALIGMENTS = ShipPosition.ALL
    ALL_COLS = GameBoard.COLS_NAMES
    ALL_ROWS = GameBoard.ROWS_NAMES

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye! Thanks for playing!")
        return True

    def do_basic(self, _):
        print(GAMEPLAY)

    def help_basic(self, _):
        print("Battleship Gameplay")

    def do_intro(self, _):
        print(INSTRUCTIONS)

    def help_intro(self, _):
        print("Battleship CLI Instructions.")

    def do_p1(self, name):
        print("Adding Player 1: '{}'".format(name))
        self.player_1 = Player(name=name)

    def help_p1(self):
        print("Set Player 1")

    def do_p2(self, name):
        print("Adding Player 2: '{}'".format(name))
        self.player_2 = Player(name=name)

    def help_p2(self):
        print("Set Player 2")

    def do_start(self, _):
        print("Starting game.")
        self.game = Game(
            player_1=self.player_1,
            player_2=self.player_2,
        )

    def help_start(self):
        print("Start game")

    def do_place_ship_p1(self, row_col_ship_aligment):
        row, col, ship, aligment = row_col_ship_aligment.split(' ')
        try:
            self.game.place_ships_for_player_1([
                ShipPosition(
                    row=row,
                    col=col,
                    ship=Ship.get_ship(ship),
                    aligment=ShipPosition.get_aligment(aligment)
                ),
            ])
            print("Placing ships for {player}: {row}{col} {ship} {aligment}".format(
                player=self.player_1.name,
                row=row,
                col=col,
                ship=Ship.get_ship(ship).NAME,
                aligment=ShipPosition.get_aligment(aligment),
            ))
        except AttributeError as exc:
            print("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            print("Error: {}".format(str(exc)))

    def help_place_ship_p1(self):
        print(
            (
                "Place ships for Player 1: Format: row col ship aligment "
                "Example: place_ship_p1 A 1 carrier h"
            )
        )

    def do_place_ship_p2(self, row_col_ship_aligment):
        row, col, ship, aligment = row_col_ship_aligment.split(' ')
        try:
            self.game.place_ships_for_player_2([
                ShipPosition(
                    row=row,
                    col=col,
                    ship=Ship.get_ship(ship),
                    aligment=ShipPosition.get_aligment(aligment)
                ),
            ])
            print("Placing ships for {player}: {row}{col} {ship} {aligment}".format(
                player=self.player_2.name,
                row=row,
                col=col,
                ship=Ship.get_ship(ship).NAME,
                aligment=ShipPosition.get_aligment(aligment),
            ))
        except AttributeError as exc:
            print("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            print("Error: {}".format(str(exc)))

    def help_place_ship_p2(self):
        print(
            (
                "Place ships for Player 2: Format: row col ship aligment "
                "Example: place_ship_p1 A 1 carrier h"
            )
        )

    def do_play(self, _):
        print("Start shooting!")
        self.game.play()

    def help_play(self):
        print("Start shooting!")

    def do_shoot_p1(self, row_col):
        row, col = row_col.split(' ')
        try:
            self.player_1.shoot(row, col)
        except AttributeError as exc:
            print("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            print("Error: {}".format(str(exc)))

    def help_shoot_p1(self):
        print(
            (
                "Shoot ships from Player 1 to Player 2: Format: row col "
                "Example: shoot_p1 A 1"
            )
        )

    def do_shoot_p2(self, row_col):
        row, col = row_col.split(' ')
        try:
            self.player_2.shoot(row, col)
        except AttributeError as exc:
            print("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            print("Error: {}".format(str(exc)))

    def help_shoot_p2(self):
        print(
            (
                "Shoot ships from Player 2 to Player 1: Format: row col "
                "Example: shoot_p2 A 1"
            )
        )

    def do_ls(self, resource):
        resource_map = {
            'ships': self.ALL_SHIPS,
            's': self.ALL_SHIPS,
            'aligments': self.ALL_ALIGMENTS,
            'a': self.ALL_ALIGMENTS,
            'rows': self.ALL_ROWS,
            'r': self.ALL_ROWS,
            'cols': self.ALL_COLS,
            'c': self.ALL_COLS,
        }
        print(resource_map[str(resource).lower()])

    def help_ls(self):
        print(
            (
                "List resource: Format: ls <resource> "
                "Example: ls ships"
            )
        )


if __name__ == "__main__":
    BattleshipCLI().cmdloop()
