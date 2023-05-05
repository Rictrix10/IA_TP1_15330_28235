class DiagonalBlocksAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __row: int
    __col: int
    __piece: int
    __option: int
    

    def __init__(self, row: int, col: int,  piece: int, option: int, peca, diagonais):
        self.__row = row
        self.__col = col
        self.__piece = piece
        self.__option = option

        self.__peca = peca
        self.__diagonais = diagonais

    def get_row(self):
        return self.__row
    
    def get_col(self):
        return self.__col

    def get_piece(self):
        return self.__piece
    
    def get_option(self):
        return self.__option
    
    def get_peca(self):
        return self.__peca
    
    def get_diagonais(self):
        return self.__diagonais