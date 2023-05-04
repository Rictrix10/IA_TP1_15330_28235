EMPTY_CELL = -1
PLAYANLE_CELL = 0
CONNECTING_CELL = 1
FIXED_CELL = 10
class Piece:

    @staticmethod
    def get_all():
        try:
            Piece.__all_pieces
        except AttributeError:
            _ = EMPTY_CELL
            o = CONNECTING_CELL
            X = PLAYANLE_CELL
            
            Piece.__all_pieces = [
                Piece([  
                    [X] 
                    ]),      
                    
                Piece([
                    [ X, X ]
                    ]),

                Piece([
                    [X, X, X],
                ]),

                Piece([
                    [ _, X],
                    [ X, X]
                    
                ]),

                Piece([
                    [X, X, X, X]
                ]),

                Piece([  
                    [_, _, X],
                    [X, X, X]   
                ]),

                Piece([  
                    [_, X, _],
                    [X, X, X],    
                ])
            ]
        return Piece.__all_pieces
    
   # player1_pieces = get_all()
   # player2_pieces = get_all()
    
    def __init__(self, cfg):
        self.__cfg = cfg

    def width(self):
        return len(self.__cfg[0])
    
    def height(self):
        return len(self.__cfg)

    def fit_in_board(self, board, x, y):
        for i in range(x, x + self.width()):
            for j in range(y, y + self.height()):
                if self.__cfg[j][i] == EMPTY_CELL:
                    continue
                if not board[j][i] == EMPTY_CELL:
                    return False
        return True


    def print(self):
        for row in self.__cfg:
            for place in row:
                if place == EMPTY_CELL or place == CONNECTING_CELL:
                    print(" ", end="")
                elif place == PLAYANLE_CELL:
                    print("■", end="")
                else:
                    raise ValueError("Invalid piece definition")
            print("")
        print("\n")
        

                          


   
    
    def flip_hor(self):
        old_cfg = self.__cfg
 
        self.__cfg = []
        for row in old_cfg:
            new_row = []
            for i in range(len(row) - 1, -1, -1):
                new_row.append(row[i])
            self.__cfg.append(new_row)


    def flip_ver(self):
        old_cfg = self.__cfg

        self.__cfg = []
        for col in range(len(old_cfg[0])):
            new_col = []
            for col_idx in range(len(old_cfg) - 1, -1, -1):
                new_col.append(old_cfg[col_idx][col])
            self.__cfg.append(new_col)


    def rotate90(self):
        old_cfg = self.__cfg
        n_rows = len(old_cfg)
        n_cols = len(old_cfg[0])

        new_cfg = [[0] * n_rows for _ in range(n_cols)]
        for i in range(n_cols):
            for j in range(n_rows):
                new_cfg[i][j] = old_cfg[n_rows-j-1][i]

            self.__cfg = new_cfg
    
    def validar_proxima_jogada(self):
        for linha in self.__cfg:
            for caractere in linha:
                if caractere != 'o':
                    return False
        return True
    

    def criar_peca(row, column):
        peca1 = [[(row, column)]]

        peca2 = [[(row, column), (row, column+1)]]

        peca3 = [[(row, column), (row, column+1), (row, column+2)]]

        peca4 = [[(row, column), (row, column+1), (row-1, column+1)]]

        peca5 = [[(row, column), (row, column+1), (row, column+2), (row, column+3)]]

        peca6 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+2)]]

        peca7 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+1)]]

        peca8 = [[(row, column), (row, column+1), (row-1, column+1), (row-1, column+2)]]

        peca9 = [[(row, column), (row, column+1), (row-1, column), (row-1, column+1)]]

        peca10 = [[(row, column), (row, column+1), (row, column+2), (row, column+3), (row, column+4)]]

        peca11 = [[(row, column), (row, column+1), (row, column+2), (row, column+3), (row-1, column+3)]]

        peca12 = [[(row, column), (row, column+1), (row, column+2), (row, column+3), (row-1, column+2)]]

        peca13 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+1), (row-1, column+2)]]

        peca14 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+2), (row-1, column+3)]]

        peca15 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+2), (row-2, column+2)]]

        peca16 = [[(row, column), (row, column+1), (row-1, column+1), (row-2, column+1), (row-2, column+2)]]

        peca17 = [[(row, column), (row, column+1), (row-1, column+1), (row-2, column+1), (row-2, column)]]

        peca18 = [[(row, column), (row, column+1), (row-1, column+1), (row-1, column+2), (row-2, column+2)]]

        peca19 = [[(row, column), (row, column+1), (row, column+2), (row+1, column+1), (row-1, column+1)]]

        peca20 = [[(row, column), (row, column+1), (row, column+2), (row-1, column+1), (row-2, column+1)]]

        peca21 = [[(row, column), (row, column+1), (row-1, column+1), (row-2, column+1), (row-1, column+2)]]

        return [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                        peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]

    def criar_diagonal(row, column):

        PECA1 = [[(row-1, column-1), (row+1, column-1), (row-1, column+1), (row+1, column+1)]]

        PECA2 = [[(row-1, column-1), (row+1, column-1), (row+1, column+2), (row-1, column+2)]]

        PECA3 = [[(row-1, column-1), (row+1, column-1), (row-1, column+3), (row+1, column+3)]]

        PECA4 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+2), (row+1, column+2)]]
        
        PECA5 = [[(row-1, column-1), (row+1, column-1), (row- 1, column +4), (row+1, column+4)]]
    
        PECA6 = [[(row-1, column-1), (row+1, column-1), (row-2, column + 1), (row-2, column+3), (row+1, column+3)]]

        PECA7 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+2), (row-1, column+3), (row+1, column+3)]]

        PECA8 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+3), (row+1, column+2), (row, column+3)]]

        PECA9 = [[(row-2, column-1), (row+1, column-1), (row-2, column+2), (row+1, column+2)]]

        PECA10 = [[(row-1, column-1), (row+1, column-1), (row-1, column+5), (row+1, column+5)]]

        PECA11 = [[(row-1, column-1), (row+1, column-1), (row-2, column+2), (row-2, column+4), (row+1, column+4)]]

        PECA12 = [[(row-1, column-1), (row+1, column-1), (row-2, column+1), (row-2, column+3), (row-1, column+4), (row+1, column+4)]]

        PECA13 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+3), (row+1, column+3)]]

        PECA14 = [[(row-1, column-1), (row+1, column-1), (row-2, column+1), (row-2, column+4), (row+1, column+3), (row, column+4)]]

        PECA15 = [[(row-1, column-1), (row+1, column-1), (row-3, column+1), (row-3, column+3), (row+1, column+3)]]

        PECA16 = [[(row-1, column-1), (row+1, column-1), (row-3, column), (row-3, column+3), (row-1, column+3), (row+1, column+2)]]

        PECA17 = [[(row-1, column-1), (row+1, column-1), (row-3, column-1), (row-3, column+2), (row+1, column+2)]]

        PECA18 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-3, column+1), (row-3, column+3), (row, column+3), (row+1, column+2)]]

        PECA19 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+2), (row-1, column+3), (row+1, column+3), (row+2, column), (row+2, column+2)]]

        PECA20 = [[(row-1, column-1), (row+1, column-1), (row-3, column), (row-3, column+2), (row+1, column+3)]]

        PECA21 = [[(row-1, column-1), (row+1, column-1), (row-3, column), (row-3, column+2), (row-2, column+3), (row, column+3), (row+1, column+2)]]

        return [PECA1, PECA2, PECA3, PECA4, PECA5, PECA6, PECA7, PECA8, PECA9, PECA10, PECA11, PECA12, PECA13, PECA14, PECA15, PECA16, PECA17, PECA18, PECA19, PECA20, PECA21]
