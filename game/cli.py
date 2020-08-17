from cmd import Cmd

from board import GameBoard
from logger import get_logger
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

    logger = get_logger()

    ALL_SHIPS = list(Ship.get_ship_map().keys())
    ALL_ALIGMENTS = ShipPosition.ALL
    ALL_COLS = GameBoard.COLS_NAMES
    ALL_ROWS = GameBoard.ROWS_NAMES

    def do_exit(self, inp):
        '''exit the application.'''
        self.logger.info("Bye! Thanks for playing!")
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
        if not name:
            self.logger.error("Name cannot be empty.".format(name))
            return None
        try:
            if str(self.player_2.name).lower() == str(name).lower():
                self.logger.error("Name '{}' already taken for the Player 2".format(name))
                return None
        except AttributeError:
            pass

        self.player_1 = Player(name=name)

    def help_p1(self):
        print("Set Player 1")

    def do_p2(self, name):
        if not name:
            self.logger.error("Name cannot be empty.".format(name))
            return None
        try:
            if str(self.player_1.name).lower() == str(name).lower():
                self.logger.error("Name '{}' already taken for the Player 1".format(name))
                return None
        except AttributeError:
            pass

        self.player_2 = Player(name=name)

    def help_p2(self):
        print("Set Player 2")

    def do_start(self, _):
        try:
            self.game = Game(
                player_1=self.player_1,
                player_2=self.player_2,
            )
        except AttributeError as exc:
            if 'player_1' in str(exc):
                self.logger.error("Game cannot start: You need to create the Player 1: p1 <name> .")

            elif 'player_2' in str(exc):
                self.logger.error("Game cannot start: You need to create the Player 2: p2 <name> .")

        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

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
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

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
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_place_ship_p2(self):
        print(
            (
                "Place ships for Player 2: Format: row col ship aligment "
                "Example: place_ship_p1 A 1 carrier h"
            )
        )

    def do_play(self, _):
        try:
            self.game.play()
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_play(self):
        print("Start shooting!")

    def do_shoot(self, row_col):
        row, col = row_col.split(' ')
        try:
            self.game.shoot(row, col)
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_shoot(self):
        print(
            (
                "Shoot ships according to the turn. Format: row col "
                "Example: shoot A 1"
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
        try:
            print(resource_map[str(resource).lower()])
        except KeyError as exc:
            self.logger.error("Resource not found: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_ls(self):
        print(
            (
                "List resource: Format: ls <resource> "
                "Example: ls ships"
            )
        )

    def do_stats(self, _):
        try:
            self.game.display_stats()
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_stats(self):
        print("Display game stats")

    def do_restart(self, _):
        try:
            self.game.restart()
        except AttributeError as exc:
            self.logger.error("Error: Game not started. Details: {}".format(str(exc)))
        except Exception as exc:
            self.logger.error("Error: {}".format(str(exc)))

    def help_restart(self):
        print("Restart the game, Using the same players.")


if __name__ == "__main__":
    BattleshipCLI().cmdloop()
