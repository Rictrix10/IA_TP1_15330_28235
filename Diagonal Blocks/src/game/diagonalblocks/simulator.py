from game.diagonalblocks.player import DiagonalBlocksPlayer
from game.diagonalblocks.state import DiagonalBlocksState
from game.game_simulator import GameSimulator


class DiagonalBlocksSimulator(GameSimulator):

    def __init__(self, player1: DiagonalBlocksPlayer, player2: DiagonalBlocksPlayer, num_rows: int = 20, num_cols: int = 20):
        super(DiagonalBlocksSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return DiagonalBlocksState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: DiagonalBlocksState):
        # ignored for this simulator
        pass

    def end_game(self, state: DiagonalBlocksState):
        # ignored for this simulator
        pass
