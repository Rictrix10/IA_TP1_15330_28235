class DiagonalBlocksAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int
    __piece: int

    def __init__(self, col: int, row: int, piece: int):
        self.__col = col
        self.__row = row
        self.__piece = piece

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row

    def get_piece(self):
        return self.__piece