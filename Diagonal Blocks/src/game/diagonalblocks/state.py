import itertools
from typing import Optional

from game.diagonalblocks.action import DiagonalBlocksAction
from game.diagonalblocks.result import DiagonalBlocksResult
from game.state import State


class DiagonalBlocksState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 20, num_cols: int = 20):
        super().__init__()

        if num_rows != 20:
            raise Exception("O número de linhas tem de ser igual a 20")
        if num_cols != 20:
            raise Exception("O número de colunas tem de ser igual a 20")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        self.__grid = [[DiagonalBlocksState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: DiagonalBlocksAction) -> bool:
        row = action.get_row()
        col = action.get_col()

        # valid row
        if row < 0 or col >= self.__num_rows:
            return False
        
        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        # full column
        if self.__grid[row][col] != DiagonalBlocksState.EMPTY_CELL:
            return False

        return True

    def update(self, action: DiagonalBlocksAction):
        row = action.get_row()
        col = action.get_col()

        # player play
        self.grid[row][col] = self.__acting_player

        # drop the checker
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.grid[row][col] = self.__acting_player
                break

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'R',
                  1: 'B',
                  DiagonalBlocksState.EMPTY_CELL: ' '
              }[self.grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DiagonalBlocksState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cloned_state.__grid[row][col] = self.grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DiagonalBlocksResult]:
        if self.__has_winner:
            return DiagonalBlocksResult.LOOSE if pos == self.__acting_player else DiagonalBlocksResult.WIN
        if self.__is_full():
            return DiagonalBlocksResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: DiagonalBlocksAction(pos[0], pos[1]),
                itertools.product(range(0, self.get_num_rows()),
                                  range(0, self.get_num_cols())))
                
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
