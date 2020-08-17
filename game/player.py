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
