from termcolor import colored

from ship import (
    Ship,
    ShipPosition,
)


class GameBoard(object):
    """docstring for GameBoard"""
    COLS_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    ROWS_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    MAX_SHIPS_PER_BOARD = 5
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
        self.log_msg('Shoots: {}'.format(len(self.player.shoots)))
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
