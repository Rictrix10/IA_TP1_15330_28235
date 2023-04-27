from random import randint

from games.diagonalblocks.action import DiagonalBlocksAction
from games.diagonalblocks.player import DiagonalBlocksPlayer
from games.diagonalblocks.state import DiagonalBlocksState
from games.state import State


class RandomDiagonalBlocksPlayer(DiagonalBlocksPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DiagonalBlocksState):

        return DiagonalBlocksAction(randint(0, state.get_num_rows()), randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
