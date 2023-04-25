class DiagonalBlocksAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __row: int
    __col: int
    __peca: int
    __subpeca: int

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col
        

    def get_row(self):
        return self.__row
    
    def get_col(self):
        return self.__col

    def get_peca(self):
        return self.__peca
    
    def get_subpeca(self):
        return self.__subpeca