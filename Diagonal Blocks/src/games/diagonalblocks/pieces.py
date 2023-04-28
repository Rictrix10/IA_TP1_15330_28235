

class Piece:

    @staticmethod
    def get_all(i, j):
        try:
            Piece.__all_pieces
        except AttributeError:
            
            Piece.__all_pieces = [
                
                Piece([[(i, j)]]),

                Piece([[(i, j), (i, j+1)]]),

                Piece([[(i, j), (i, j+1), (i, j+2)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i, j+3)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+2)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+1)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2)]]),

                Piece([[(i, j), (i, j+1), (i-1, j), (i-1, j+1)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i, j+3), (i, j+4)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+3)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i, j+3), (i-1, j+2)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+2)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-1, j+3)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+2), (i-2, j+2)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j+2)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-2, j)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1), (i-1, j+2), (i-2, j+2)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i+1, j+1), (i-1, j+1)]]),

                Piece([[(i, j), (i, j+1), (i, j+2), (i-1, j+1), (i-2, j+1)]]),

                Piece([[(i, j), (i, j+1), (i-1, j+1), (i-2, j+1), (i-1, j+2)]])
                    
                ]
            
        return Piece.__all_pieces

    def __init__(self, cfg):
        self.__cfg = cfg

    
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
    

