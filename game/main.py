from board import GameBoard
from logger import get_logger
from player import Player
from ship import (
    Battleship,
    Carrier,
    ShipPosition,
)


class Game(object):

    PLAYER_1_COLOR = 'cyan'
    PLAYER_2_COLOR = 'yellow'

    GAME_STARTED = 'started'
    GAME_PLAY = 'play'
    GAME_OVER = 'over'

    def __init__(self, player_1, player_2):
        self.logger = get_logger()
        self.logger.info("Starting game...")
        # Players
        self.player_1 = player_1
        self.player_2 = player_2
        # Boards
        self.logger.info("Creating boards...")
        self.board_1 = GameBoard(player=self.player_1, color=self.PLAYER_1_COLOR)
        self.board_2 = GameBoard(player=self.player_2, color=self.PLAYER_2_COLOR)
        # Set the opponents
        self.logger.info("Assingning opponents...")
        self.player_1.set_opponent_board(self.board_2)
        self.player_2.set_opponent_board(self.board_1)
        self.logger.info('Game started. Start placing ships!')
        self.status = self.GAME_STARTED

    def play(self):
        if not self.board_1.get_all_ships() or not self.board_2.get_all_ships():
            raise Exception('No ships added. You have to place some ships before to start playing.')
        self.logger.info('Locking boards...')
        self.board_1.lock_board()
        self.board_2.lock_board()
        self.logger.info('Done. You cannot add more ships.')
        self.player_1.reverse_turn()
        self.logger.info("Start shooting {p1}! Then {p2} is your turn.".format(
            p1=self.player_1.name,
            p2=self.player_2.name,
        ))
        self.status = self.GAME_PLAY

    def reverse_turns(self):
        self.player_1.reverse_turn()
        self.player_2.reverse_turn()

    def place_ships_for_player_1(self, ship_locations):
        if self.status != self.GAME_STARTED:
            raise Exception("Game not started. You have to register the players and start a new game first.")
        for ship_position in ship_locations:
            self.board_1.place_ship(**ship_position.export())
            self.logger.info("Placing ships for {player}: {row}{col} {ship} {aligment}".format(
                player=self.player_1.name,
                row=ship_position.row,
                col=ship_position.col,
                ship=ship_position.ship.NAME,
                aligment=ship_position.aligment,
            ))
        self.logger.info("Are you ready? switch to play mode to start shooting!")

    def place_ships_for_player_2(self, ship_locations):
        if self.status != self.GAME_STARTED:
            raise Exception("Game not started. You have to register the players and start a new game first.")
        for ship_position in ship_locations:
            self.board_2.place_ship(**ship_position.export())
            self.logger.info("Placing ships for {player}: {row}{col} {ship} {aligment}".format(
                player=self.player_2.name,
                row=ship_position.row,
                col=ship_position.col,
                ship=ship_position.ship.NAME,
                aligment=ship_position.aligment,
            ))
        self.logger.info("Are you ready? switch to play mode to start shooting!")

    def shoot(self, row, col):
        if self.status == self.GAME_OVER:
            raise Exception('Game over! restart the game to continue playing.')
        if self.status == self.GAME_STARTED:
            raise Exception('You have to switch to play mode to start shooting!')

        if self.player_1.is_my_turn:
            self.player_1.shoot(row, col)
            self.logger.info("Go ahead {}! it's your turn.".format(self.player_2.name))
        elif self.player_2.is_my_turn:
            self.player_2.shoot(row, col)
            self.logger.info("Go ahead {}! it's your turn.".format(self.player_1.name))
        self.reverse_turns()

        if self.board_1.are_all_ships_sunk:
            self.logger.info('Player {} wins!'.format(self.player_2.name))
            self.status = self.GAME_OVER
        elif self.board_2.are_all_ships_sunk:
            self.logger.info('Player {} wins!'.format(self.player_1.name))
            self.status = self.GAME_OVER

    def display_stats(self):
        self.board_1.display_shoots()
        self.board_1.display_ship_statuses()

        self.board_2.display_shoots()
        self.board_2.display_ship_statuses()

        if self.board_1.are_all_ships_sunk:
            self.logger.info('Player {} wins!'.format(self.player_2.name))
        elif self.board_2.are_all_ships_sunk:
            self.logger.info('Player {} wins!'.format(self.player_1.name))

    def restart(self):
        self.board_1.unlock_board()
        self.board_2.unlock_board()
        self.board_1.init_board()
        self.board_2.init_board()
        self.player_1.reset_shoots()
        self.player_2.reset_shoots()
        self.player_1.reset_turns()
        self.player_2.reset_turns()
        self.status = self.GAME_STARTED
        self.logger.info('Game restarted. Start placing ships!')


def demo_match():
    # Create players
    player_1 = Player(name='Player 1')
    player_2 = Player(name='Player 2')
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
    game.shoot('A', '3')
    game.shoot('D', '4')
    game.shoot('A', '4')
    game.shoot('E', '4')
    game.shoot('A', '5')
    game.shoot('F', '4')
    game.shoot('A', '6')
    game.shoot('G', '4')
    game.shoot('A', '6')
    game.shoot('H', '4')
    game.shoot('A', '8')
    game.shoot('A', '3')
    game.shoot('D', '4')
    game.shoot('A', '4')
    game.shoot('E', '4')
    game.shoot('F', '4')
    game.shoot('G', '4')
    game.shoot('H', '4')

    # Display stats
    game.display_stats()


if __name__ == "__main__":
    demo_match()
