import itertools
from typing import Optional

from games.diagonalblocks.action import DiagonalBlocksAction
from games.diagonalblocks.result import DiagonalBlocksResult
from games.state import State
from games.diagonalblocks.piece import Piece


class DiagonalBlocksState(State):
    EMPTY_CELL = -1
    DOT_CELLR = -2
    DOT_CELLB = -3

    '''
    def __init__(self, num_rows: int = 20, num_cols: int = 20):
        super().__init__()

        if num_rows < 20:
            raise Exception("the number of rows must be 20")
        if num_cols < 20:
            raise Exception("the number of rows must be 20")
    '''

    def __init__(self, size: int = 3):
        super().__init__()

        if size < 3:
            raise Exception("the number of rows must be 20")

        """
        the dimensions of the board
        """
        self.size = size
        self.num_rows = size
        self.num_cols = size

        """
        the grid
        """
        
       

        self.grid = [[DiagonalBlocksState.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]

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

    def validate_action(self, action: DiagonalBlocksAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        piece = action.get_piece()
        option = action.get_option()

        # valid column
        if col < 0 or col >= self.num_cols:
            return False

        # valid row
        if row < 0 or row >= self.num_rows:
            return False

        # full column
        if self.grid[row][col] != DiagonalBlocksState.EMPTY_CELL:
            return False

        if piece < 0 or piece > 20:
            return False
        
        return True

    def update(self, action: DiagonalBlocksAction):
        col = action.get_col()
        row = action.get_row()
        piece = action.get_piece()
        peca_selecionada = action.get_peca()
        diagonais_selecionadas = action.get_diagonais()

        '''
        peca = Piece.criar_peca(row, col)
        peca_selecionada = peca[piece][0]
        diagonais = Piece.criar_diagonal(row, col)
        diagonais_selecionadas = diagonais[piece][0]
        #'''
        
        for x in range(len(peca_selecionada)):
            row = peca_selecionada[x][0]
            col = peca_selecionada[x][1]
            self.grid[row][col] = self.__acting_player

        for x in range(len(diagonais_selecionadas)):
            row = diagonais_selecionadas[x][0]
            col = diagonais_selecionadas[x][1]
            if self.__acting_player == 0:
                self.grid[row][col] = DiagonalBlocksState.DOT_CELLR
            else:
                self.grid[row][col] = DiagonalBlocksState.DOT_CELLB
        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

        
        
    def __display_cell(self, row, col):
        print({
            0: '\033[91m▩\033[0m',   #  0: 'R',
            1: '\033[96m▩\033[0m',   #  1: 'B',
            DiagonalBlocksState.EMPTY_CELL: ' ',
            DiagonalBlocksState.DOT_CELLR: '\033[91m○\033[0m',
            DiagonalBlocksState.DOT_CELLB: '\033[96m○\033[0m'
        }[self.grid[row][col]], end="")


    def __display_numbers(self):
        for col in range(0, self.num_cols):
            if col < 20:
                if col < 10:
                    print('', end="  ")
                else: 
                    print('', end=" ")
            print(col, end=" ")
        print("")

        #for row in range(0, self.num_rows):
         #   if row < 20:
          #      print(' ', end=" ")
           # print(row, end="")
        #print("")

    def __display_separator(self):
        for col in range(0, self.num_cols):
            print("----", end="")
        print("--")
    
    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.num_rows):
            print('|', end=" ")
            for col in range(0, self.num_cols):
                self.__display_cell(row, col)
                print(' | ', end="")
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
        cloned_state = DiagonalBlocksState(self.num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cloned_state.grid[row][col] = self.grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DiagonalBlocksResult]:
        if self.__has_winner:
            return DiagonalBlocksResult.LOOSE if pos == self.__acting_player else DiagonalBlocksResult.WIN
        if self.__is_full():
            return DiagonalBlocksResult.DRAW
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
                lambda position: DiagonalBlocksAction(position[0], position[1]),
                itertools.product(range(0, self.get_num_rows()),
                                  range(0, self.get_num_cols())))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
