from board import GameBoard
from logger import get_logger
from player import Player
from ship import (
    Battleship,
    Carrier,
    ShipPosition,
)


class Game(object):

    def __init__(self, player_1, player_2):
        self.logger = get_logger()
        # Players
        self.player_1 = player_1
        self.player_2 = player_2
        # Boards
        self.board_1 = GameBoard(player=self.player_1, color='green')
        self.board_2 = GameBoard(player=self.player_2, color='yellow')
        # Set the opponents
        self.player_1.set_opponent_board(self.board_2)
        self.player_2.set_opponent_board(self.board_1)
        self.logger.info('Game initiated.')

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


def main(p1, p2):
    # Create players
    player_1 = Player(name=p1)
    player_2 = Player(name=p2)
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
