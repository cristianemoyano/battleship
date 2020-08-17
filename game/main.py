"""
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
"""
from decimal import Decimal

from termcolor import colored


class Player(object):
    """docstring for Player"""
    def __init__(self, name):
        self.name = name
        self._shoots = []
        self._opponent_board = None

    def set_opponent_board(self, opponent_board):
        self._opponent_board = opponent_board

    def shoot(self, row, col):
        result = self._opponent_board.shoot(row, col)
        self._shoots.append({
            'row': row,
            'col': col,
            'result': result,
        })

    @property
    def shoots(self):
        return self._shoots


class Ship(object):
    """Ship"""

    LENGH = None
    NAME = 'Base Ship'

    def __init__(self):
        self._status = 0

    def __repr__(self):
        print(self.NAME)

    def __str__(self):
        return self.NAME

    @property
    def status(self):
        status = (Decimal(self._status) * Decimal(100)) / Decimal(self.LENGH)
        return '{} %'.format(status)

    @property
    def is_sunk(self):
        return self._status == self.LENGH

    def damage(self, msg_color='green'):
        if not self.is_sunk:
            self._status += 1


class Carrier(Ship):
    """Ship"""

    LENGH = 5
    NAME = 'Carrier'


class Battleship(Ship):
    """Ship"""

    LENGH = 4
    NAME = 'Battleship'


class Cruiser(Ship):
    """Ship"""

    LENGH = 3
    NAME = 'Cruiser'


class Submarine(Ship):
    """Ship"""

    LENGH = 3
    NAME = 'Submarine'


class Destroyer(Ship):
    """Ship"""

    LENGH = 2
    NAME = 'Destroyer'


class ShipPosition(object):
    """docstring for Position"""

    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    ALL = [HORIZONTAL, VERTICAL]

    def __init__(self, row, col, ship, aligment):
        self.row = row
        self.col = col
        self.ship = ship
        self.aligment = aligment

    def export(self):
        return {
            'row': self.row,
            'col': self.col,
            'ship': self.ship,
            'aligment': self.aligment,
        }


class GameBoard(object):
    """docstring for GameBoard"""
    COLS_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    ROWS_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    MAX_SHIPS_PER_BOARD = 2
    VALID_POSITIONS = ShipPosition.ALL

    HIT = 'X'
    MISS = '*'

    def __init__(self, player, color):
        self.is_board_locked = False
        self.board = self.init_board()
        self.player = player
        self.color = color

    def get_col_index(self, value):
        return self.COLS_NAMES.index(value)

    def get_col_value(self, index):
        return self.COLS_NAMES[index]

    def get_row_index(self, value):
        return self.ROWS_NAMES.index(value)

    def get_row_value(self, index):
        return self.ROWS_NAMES[index]

    def init_board(self):
        # Returns Dict: { ('row', 'col'): {}  }
        return {(row, col): {} for col in self.COLS_NAMES for row in self.ROWS_NAMES}

    def _validate_place_params(self, row, col, ship, aligment):
        row = str(row).upper()
        col = str(col).upper()
        is_valid_row = row in self.ROWS_NAMES
        is_valid_col = col in self.COLS_NAMES
        is_valid_coordinate = is_valid_col and is_valid_row
        if not is_valid_coordinate:
            raise Exception('Invalid coordinate sent: {row}{col}.'.format(row=row, col=col))

        aligment = str(aligment).lower()
        if aligment not in self.VALID_POSITIONS:
            raise Exception('Invalid position sent: {}.'.format(aligment))

        if not isinstance(ship, Ship):
            raise Exception('Invalid ship sent: {}.'.format(str(ship)))

        if self.is_board_locked:
            raise Exception('The board is locked, you cannot place another ship.')

        # check places:
        try:
            if aligment == ShipPosition.HORIZONTAL:
                # Place ship in horizontal position, populating in right direction
                for i in range(self.get_col_index(col), ship.LENGH + self.get_col_index(col)):
                    if self.board[(row, self.get_col_value(i))]:
                        raise Exception(
                            'Invalid place -  Ships can touch each other, but they cannot occupy the same grid space.'
                        )
            elif aligment == ShipPosition.VERTICAL:
                # Place ship in vertical position, populating in down direction
                for i in range(self.get_row_index(row), ship.LENGH + self.get_row_index(row)):
                    if self.board[(self.get_row_value(i), col)]:
                        raise Exception(
                            'Invalid place -  Ships can touch each other, but they cannot occupy the same grid space.'
                        )
        except IndexError:
            raise Exception('Invalid place - Ships cannot be placed off the board.')
        # Validate max number of ships
        if len(self.get_all_ships()) == self.MAX_SHIPS_PER_BOARD:
            raise Exception('Maximum number of ships reached.')

    def get_all_ships(self):
        all_ships = []
        for coord, ship in self.board.items():
            if not ship or ship in all_ships:
                continue
            all_ships.append(ship)
        return all_ships

    def place_ship(self, row, col, ship, aligment):
        """
          |  1    2    3    4    5
        ---------------------------
        A | A 1  A 2  A 3  A 4  A 5
        B | B 1
        C | C 1
        D | D 1
        E | E 1
        F | F 1
        """
        self._validate_place_params(row, col, ship, aligment)

        if aligment == ShipPosition.HORIZONTAL:
            # Place ship in horizontal position, populating in right direction
            for i in range(self.get_col_index(col), ship.LENGH + self.get_col_index(col)):
                self.board[(row, self.get_col_value(i))] = ship
        elif aligment == ShipPosition.VERTICAL:
            # Place ship in vertical position, populating in down direction
            for i in range(self.get_row_index(row), ship.LENGH + self.get_row_index(row)):
                self.board[(self.get_row_value(i), col)] = ship

    def shoot(self, row, col):
        if not self.is_board_locked:
            raise Exception('Game is not started yet. - You cannot start shooting before to start.')
        ship = self.board.get((row, col))
        if ship:
            ship.damage()
            self.log_msg('Agg! You hit me ! {}'.format(ship.status))
            if ship.is_sunk:
                self.log_msg('Ohh! You sunk my {}'.format(ship.NAME))
            return self.HIT
        else:
            self.log_msg('Uff! You failed!')
            return self.MISS

    def display_shoots(self):
        self.log_msg('Shoots: {} \n'.format(len(self.player.shoots)))
        for shoot in self.player.shoots:
            self.log_msg('{row}{col} : {re}'.format(row=shoot['row'], col=shoot['col'], re=shoot['result'],))

    def display_ship_statuses(self):
        all_ships = self.get_all_ships()
        for ship in all_ships:
            self.log_msg('Ship {name} {status}'.format(name=ship.NAME, status=ship.status))

    def lock_board(self):
        self.is_board_locked = True

    def log_msg(self, msg):
        print(colored('{name} - {msg}'.format(name=self.player.name, msg=msg), self.color))

    def display_board(self):
        self.log_msg('----- START BOARD -----\n')
        all_ships = []
        for coord, ship in self.board.items():
            if not ship:
                continue
            if ship not in all_ships:
                all_ships.append(ship)
            self.log_msg('{coord} - {ship}'.format(coord=coord, ship=str(ship)))
        self.log_msg('Total ships: {} \n'.format(len(all_ships)))
        self.log_msg('----- END BOARD -----\n')

    @property
    def are_all_ships_sunk(self):
        return all([ship.is_sunk for ship in self.get_all_ships()])


class Game(object):

    def __init__(self, player_1, player_2):
        # Players
        self.player_1 = player_1
        self.player_2 = player_2
        # Boards
        self.board_1 = GameBoard(player=self.player_1, color='green')
        self.board_2 = GameBoard(player=self.player_2, color='yellow')
        # Set the opponents
        self.player_1.set_opponent_board(self.board_2)
        self.player_2.set_opponent_board(self.board_1)

    def play(self):
        self.board_1.lock_board()
        self.board_2.lock_board()

    def place_ships_for_player_1(self, ship_locations):
        for ship_position in ship_locations:
            self.board_1.place_ship(**ship_position.export())

    def place_ships_for_player_2(self, ship_locations):
        for ship_position in ship_locations:
            self.board_2.place_ship(**ship_position.export())

    def display_stats(self):
        self.board_1.display_board()
        self.board_2.display_board()
        self.board_1.display_shoots()
        self.board_2.display_shoots()
        self.board_1.display_ship_statuses()
        self.board_2.display_ship_statuses()

        if self.board_1.are_all_ships_sunk:
            print('Player {} wins!'.format(self.player_2.name))
        elif self.board_2.are_all_ships_sunk:
            print('Player {} wins!'.format(self.player_1.name))


def main():
    # Create players
    player_1 = Player(name='Cristian')
    player_2 = Player(name='Emanuel')
    # Initiate the game
    game = Game(
        player_1=player_1,
        player_2=player_2,
    )
    # Place the ships
    game.place_ships_for_player_1([
        ShipPosition(row='A', col='3', ship=Carrier(), aligment=ShipPosition.HORIZONTAL),
        ShipPosition(row='D', col='4', ship=Battleship(), aligment=ShipPosition.VERTICAL),
    ])
    game.place_ships_for_player_2([
        ShipPosition(row='A', col='3', ship=Carrier(), aligment=ShipPosition.HORIZONTAL),
        ShipPosition(row='D', col='4', ship=Battleship(), aligment=ShipPosition.VERTICAL),
    ])
    game.play()
    # Game play
    player_1.shoot('A', '3')
    player_1.shoot('A', '4')
    player_1.shoot('A', '5')
    player_1.shoot('A', '6')
    player_1.shoot('A', '6')
    player_1.shoot('A', '8')
    player_1.shoot('D', '4')
    player_1.shoot('E', '4')
    player_1.shoot('F', '4')
    player_1.shoot('G', '4')
    player_1.shoot('H', '4')

    player_2.shoot('D', '4')
    player_2.shoot('E', '4')
    player_2.shoot('F', '4')
    player_2.shoot('G', '4')
    player_2.shoot('H', '4')
    player_2.shoot('A', '3')
    player_2.shoot('A', '4')

    # Display stats
    game.display_stats()


if __name__ == "__main__":
    main()
