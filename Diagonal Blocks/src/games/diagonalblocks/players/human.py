from games.diagonalblocks.action import DiagonalBlocksAction
from games.diagonalblocks.player import DiagonalBlocksPlayer
from games.diagonalblocks.state import DiagonalBlocksState


class HumanDiagonalBlocksPlayer(DiagonalBlocksPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DiagonalBlocksState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                row = (int(input(f"Player {state.get_acting_player()}, choose a row: ")))
                column = (int(input(f"Player {state.get_acting_player()}, choose a column: ")))
                return DiagonalBlocksAction(column, row)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: DiagonalBlocksState):
        # ignore
        pass

    def event_end_game(self, final_state: DiagonalBlocksState):
        # ignore
        pass
