import itertools
from typing import Optional

from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult
from games.state import State


class TicTacToeState(State):
    EMPTY_CELL = -1

    def __init__(self, size: int = 3):
        super().__init__()



        if size < 3:
            raise Exception("the number of rows must be 3")


        """
        the dimensions of the board
        """
        self.size = size
        self.num_rows = size
        self.num_cols = size

        """
        the grid
        """
        self.grid = [[TicTacToeState.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]

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

            # check for horizontal win
            for row in range(self.num_rows):
                for col in range(self.num_cols - (self.size - 1)):
                    if all(self.grid[row][col + i] == player for i in range(self.size)):
                        return True

            # check for vertical win
            for row in range(self.num_rows - (self.size - 1)):
                for col in range(self.num_cols):
                    if all(self.grid[row + i][col] == player for i in range(self.size)):
                        return True

            # check for diagonal win (top-left to bottom-right)
            for row in range(self.num_rows - (self.size - 1)):
                for col in range(self.num_cols - (self.size - 1)):
                    if all(self.grid[row + i][col + i] == player for i in range(self.size)):
                        return True

            # check for diagonal win (bottom-left to top-right)
            for row in range(self.size - 1, self.num_rows):
                for col in range(self.num_cols - (self.size - 1)):
                    if all(self.grid[row - i][col + i] == player for i in range(self.size)):
                        return True

            return False

    def get_grid(self):
        return self.grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: TicTacToeAction) -> bool:
        col = action.get_col()
        row = action.get_row()


        # valid column
        if col < 0 or col >= self.num_cols:
            return False

        # valid row
        if row < 0 or row >= self.num_rows:
            return False

        # full column
        if self.grid[row][col] != TicTacToeState.EMPTY_CELL:
            return False

        return True

    def update(self, action: TicTacToeAction):
        col = action.get_col()
        row = action.get_row()

        # player play
        self.grid[row][col] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'X',
                  1: 'O',
                  TicTacToeState.EMPTY_CELL: ' '
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

        for row in range(0, self.num_rows):
            print('|', end="")
            for col in range(0, self.num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.num_cols * self.num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = TicTacToeState(self.num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cloned_state.grid[row][col] = self.grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[TicTacToeResult]:
        if self.__has_winner:
            return TicTacToeResult.LOOSE if pos == self.__acting_player else TicTacToeResult.WIN
        if self.__is_full():
            return TicTacToeResult.DRAW
        return None

    def get_num_rows(self):
        return self.num_rows

    def get_num_cols(self):
        return self.num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda position: TicTacToeAction(position[0], position[1]),
                itertools.product(range(0, self.get_num_rows()),
                                  range(0, self.get_num_cols())))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
