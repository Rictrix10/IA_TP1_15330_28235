EMPTY_CELL = -1
PLAYANLE_CELL = 0
CONNECTING_CELL = 1

class Peca:

    @staticmethod
    def get_all():
        try:
            Peca.__all_pieces
        except AttributeError:
            _ = EMPTY_CELL
            o = CONNECTING_CELL
            X = PLAYANLE_CELL
            
            Peca.__all_pieces = [
                Peca([
                    [o, _, o],
                    [_, X, _],
                    [o, _, o]
                ]),
                Peca([
                    [o, _, _, o],
                    [_, X, X, _],
                    [o, _, _, o]
                ]),

                Peca([
                    [o, _, _, _, o],
                    [_, X, X, X, _],
                    [o, _, _, _, o]
                ]),

                Peca([
                    [_, o, _, o],
                    [o, _, X, _],
                    [_, X, X, _],
                    [o, _, _, o]
                ]),

                Peca([
                    [o, _, _, _, _, o],
                    [_, X, X, X, X, _],
                    [o, _, _, _, _, o]
                ]),

                Peca([
                    [_, _, o, _, o],
                    [o, _, _, X, _],
                    [_, X, X, X, _],
                    [o, _, _, _, o]
                ]),

                Peca([
                    [_, o, _, o, _],
                    [o, _, X, _, o],
                    [_, X, X, X, _],
                    [o, _, _, _, o]
                ])
            ]
        return Peca.__all_pieces

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
                    print("▮", end="")
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


    print("teste")
