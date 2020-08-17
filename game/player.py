from logger import get_logger


class Player(object):
    """docstring for Player"""
    def __init__(self, name):
        self.logger = get_logger()
        self.reset_turns()
        self.name = name
        self.reset_shoots()
        self._opponent_board = None
        self.logger.info("Player: '{}' created.".format(name))

    def set_opponent_board(self, opponent_board):
        self._opponent_board = opponent_board

    def reset_shoots(self):
        self._shoots = []

    def reset_turns(self):
        self._is_my_turn = False

    @property
    def is_my_turn(self):
        return self._is_my_turn

    def reverse_turn(self):
        self._is_my_turn = not self._is_my_turn

    def shoot(self, row, col):
        if self.is_my_turn:
            result = self._opponent_board.shoot(row, col)
            self._shoots.append({
                'row': row,
                'col': col,
                'result': result,
            })
        else:
            raise Exception('Wait {}! Is not your turn.'.format(self.name))

    @property
    def shoots(self):
        return self._shoots
