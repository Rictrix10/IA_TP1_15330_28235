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
            Y = FIXED_CELL
            
            Piece.__all_pieces = [
                Piece([
                    [o, _, o],
                    [_, Y, _],
                    [o, _, o]
                ]),
                Piece([
                    [o, _, _, o],
                    [_, Y, X, _],
                    [o, _, _, o]
                ]),

                Piece([
                    [o, _, _, _, o],
                    [_, Y, X, X, _],
                    [o, _, _, _, o]
                ]),

                Piece([
                    [_, o, _, o],
                    [o, _, X, _],
                    [_, Y, X, _],
                    [o, _, _, o]
                ]),

                Piece([
                    [o, _, _, _, _, o],
                    [_, Y, X, X, X, _],
                    [o, _, _, _, _, o]
                ]),

                Piece([
                    [_, _, o, _, o],
                    [o, _, _, X, _],
                    [_, Y, X, X, _],
                    [o, _, _, _, o]
                ]),

                Piece([
                    [_, o, _, o, _],
                    [o, _, X, _, o],
                    [_, Y, X, X, _],
                    [o, _, _, _, o]
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
                elif place == PLAYANLE_CELL or place == FIXED_CELL:
                    print("■", end="")
                else:
                    raise ValueError("Invalid piece definition")
            print("")

    

                
                 


   
    
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
    

