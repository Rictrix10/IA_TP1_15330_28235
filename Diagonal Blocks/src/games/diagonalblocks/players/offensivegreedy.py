from random import choice
from games.diagonalblocks.action import TicTacToeAction
from games.diagonalblocks.player import TicTacToePlayer
from games.diagonalblocks.state import TicTacToeState
from games.state import State


class OffensiveGreedyPlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        grid = state.get_grid()

        selected_col = None
        selected_row = None
        max_count = 0

        for col in range(0, state.get_num_cols()):
            for row in range(0, state.get_num_rows()):
                if not state.validate_action(TicTacToeAction(row, col)):
                    continue

                count = 0
                for r in range(0, state.get_num_rows()):
                    if grid[r][col] == self.get_current_pos():
                        count += 1


                # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_row = row
                    selected_col = col
                    max_count = count

        max_count = 0

        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if not state.validate_action(TicTacToeAction(row, col)):
                    continue

                count = 0
                for c in range(0, state.get_num_cols()):
                    if grid[row][c] == self.get_current_pos():
                        count += 1

                # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if selected_row is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_row = row
                    selected_col = col
                    max_count = count

        max_count = 0

        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if not state.validate_action(TicTacToeAction(col, col)):
                    continue

                count = 0
                for c in range(0, state.get_num_cols()):
                    if grid[c][c] == self.get_current_pos():
                        count += 1

                # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if count > max_count or (count == max_count and choice([False, True])):
                    selected_row = row
                    selected_col = col
                    max_count = count

        max_count = 0

        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if not state.validate_action(TicTacToeAction(col, col)):
                    continue

                count = 0
                for c in range(0, state.get_num_cols()):
                    if grid[::-1][c][c] == self.get_current_pos():
                        count += 1

                # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if count > max_count or (count == max_count and choice([False, True])):
                    selected_row = row
                    selected_col = col
                    max_count = count




        if selected_row is None:
            raise Exception("There is no valid action")

        if selected_col is None:
            raise Exception("There is no valid action")

        return TicTacToeAction(selected_row, selected_col)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
