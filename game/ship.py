from decimal import Decimal


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

    @staticmethod
    def get_ship_map():
        return {
            'carrier': Carrier,
            'battleship': Battleship,
            'cruiser': Cruiser,
            'submarine': Submarine,
            'destroyer': Destroyer,
        }

    @classmethod
    def get_ship(cls, name):
        return cls.get_ship_map()[str(name).lower()]()

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

    HORIZONTAL = 'h'
    VERTICAL = 'v'
    ALL = [HORIZONTAL, VERTICAL]

    @classmethod
    def get_aligment(cls, aligment):
        aligments_map = {
            'h': cls.HORIZONTAL,
            'v': cls.VERTICAL,
        }
        return aligments_map[str(aligment).lower()]

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
