from games.diagonalblocks.player import DiagonalBlocksPlayer
from games.diagonalblocks.state import DiagonalBlocksState
from games.game_simulator import GameSimulator


class DiagonalBlocksSimulator(GameSimulator):

    def __init__(self, player1: DiagonalBlocksPlayer, player2: DiagonalBlocksPlayer, size: int = 3):
        super(DiagonalBlocksSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the tictactoe grid
        """
        self.__num_rows = size

    def init_game(self):
        return DiagonalBlocksState(self.__num_rows)

    def before_end_game(self, state: DiagonalBlocksState):
        # ignored for this simulator
        pass

    def end_game(self, state: DiagonalBlocksState):
        # ignored for this simulator
        pass
