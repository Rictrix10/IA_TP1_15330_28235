EMPTY_CELL = -1
PLAYANLE_CELL = 0


from games.state import State

class Piece:

    @staticmethod
    def get_all():
        try:
            Piece.__all_pieces
        except AttributeError:
            _ = EMPTY_CELL
            X = PLAYANLE_CELL

            Piece.__all_pieces = [
                Piece([
                    [X]
                ]),

                Piece([
                    [X, X]
                ]),

                Piece([
                    [X, X, X]
                ]),

                Piece([
                    [_, X],
                    [X, X]
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
                    [X, X, X]
                ]),

                Piece([
                    [_, X, X],
                    [X, X, _]
                ]),
                Piece([
                    [X, X],
                    [X, X]
                ]),
                Piece([
                    [X, X, X, X, X]
                ]),

                Piece([
                    [_, _, _, X],
                    [X, X, X, X]
                ]),

                Piece([
                    [_, _, X, _],
                    [X, X, X, X]
                ]),

                Piece([
                    [_, X, X],
                    [X, X, X]
                ]),
                Piece([
                    [_, _, X, X],
                    [X, X, X, _]
                ]),
                Piece([
                    [_, _, X],
                    [_, _, X],
                    [X, X, X]
                ]),
                Piece([
                    [_, X, X,],
                    [_, X, _,],
                    [X, X, _,]
                ]),
                Piece([
                    [X, X],
                    [_, X],
                    [X, X]
                ]),
                Piece([
                    [_, _, X],
                    [_, X, X],
                    [X, X, _]
                ]),
                Piece([
                    [_, X, _],
                    [X, X, X],
                    [_, X, _]
                ]),
                Piece([
                    [_, X, _],
                    [_, X, _],
                    [X, X, X]
                ]),
                Piece([
                    [_, X, _],
                    [_, X, X],
                    [X, X, _]
                ])

            ]
        return Piece.__all_pieces

   # player1_pieces = get_all()
   # player2_pieces = get_all()

    def __init__(self, cfg):
        self.__original_cfg = cfg
        self.__cfg = cfg

    def show_pieces(self):
        self.grid = [[Piece.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]
        

    def print(self):
        for row in self.__cfg:
            for place in row:
                if place == EMPTY_CELL:
                    print(" ", end="")
                elif place == PLAYANLE_CELL:
                    print("◼", end="")
            print("")
        print("\t")

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

    def rotate_direita(self):
        old_cfg = self.__cfg
        n_rows = len(old_cfg)
        n_cols = len(old_cfg[0])

        new_cfg = [[0] * n_rows for _ in range(n_cols)]
        for i in range(n_cols):
            for j in range(n_rows):
                new_cfg[i][j] = old_cfg[n_rows-j-1][i]

            self.__cfg = new_cfg

    def rotate_esquerda(self):
        old_cfg = self.__cfg
        n_rows = len(old_cfg)
        n_cols = len(old_cfg[0])

        new_cfg = [[0] * n_rows for _ in range(n_cols)]
        for i in range(n_cols):
            for j in range(n_rows):
                new_cfg[i][j] = old_cfg[j][n_cols-i-1]

        self.__cfg = new_cfg

    def reset(self):
        self.__cfg = self.__original_cfg

    def criar_peca(row, column):
        peca1 = [[(row, column)]]

        peca2 = [[(row, column), (row, column+1)]]

        peca3 = [[(row, column), (row, column+1), (row, column+2)]]

        peca4 = [[(row, column), (row, column+1), (row-1, column+1)]]

        peca5 = [[(row, column), (row, column+1),
                  (row, column+2), (row, column+3)]]

        peca6 = [[(row, column), (row, column+1),
                  (row, column+2), (row-1, column+2)]]

        peca7 = [[(row, column), (row, column+1),
                  (row, column+2), (row-1, column+1)]]

        peca8 = [[(row, column), (row, column+1),
                  (row-1, column+1), (row-1, column+2)]]

        peca9 = [[(row, column), (row, column+1),
                  (row-1, column), (row-1, column+1)]]

        peca10 = [[(row, column), (row, column+1), (row, column+2),
                   (row, column+3), (row, column+4)]]

        peca11 = [[(row, column), (row, column+1), (row, column+2),
                   (row, column+3), (row-1, column+3)]]

        peca12 = [[(row, column), (row, column+1), (row, column+2),
                   (row, column+3), (row-1, column+2)]]

        peca13 = [[(row, column), (row, column+1), (row, column+2),
                   (row-1, column+1), (row-1, column+2)]]

        peca14 = [[(row, column), (row, column+1), (row, column+2),
                   (row-1, column+2), (row-1, column+3)]]

        peca15 = [[(row, column), (row, column+1), (row, column+2),
                   (row-1, column+2), (row-2, column+2)]]

        peca16 = [[(row, column), (row, column+1), (row-1, column+1),
                   (row-2, column+1), (row-2, column+2)]]

        peca17 = [[(row, column), (row, column+1), (row-1, column+1),
                   (row-2, column+1), (row-2, column)]]

        peca18 = [[(row, column), (row, column+1), (row-1, column+1),
                   (row-1, column+2), (row-2, column+2)]]

        peca19 = [[(row, column), (row, column+1), (row, column+2),
                   (row+1, column+1), (row-1, column+1)]]

        peca20 = [[(row, column), (row, column+1), (row, column+2),
                   (row-1, column+1), (row-2, column+1)]]

        peca21 = [[(row, column), (row, column+1), (row-1, column+1),
                   (row-2, column+1), (row-1, column+2)]]

        return [peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9, peca10,
                peca11, peca12, peca13, peca14, peca15, peca16, peca17, peca18, peca19, peca20, peca21]

    def criar_diagonal(row, column):

        PECA1 = [[(row-1, column-1), (row+1, column-1),
                  (row-1, column+1), (row+1, column+1)]]

        PECA2 = [[(row-1, column-1), (row+1, column-1),
                  (row+1, column+2), (row-1, column+2)]]

        PECA3 = [[(row-1, column-1), (row+1, column-1),
                  (row-1, column+3), (row+1, column+3)]]

        PECA4 = [[(row-1, column-1), (row+1, column-1),
                  (row-2, column), (row-2, column+2), (row+1, column+2)]]

        PECA5 = [[(row-1, column-1), (row+1, column-1),
                  (row - 1, column + 4), (row+1, column+4)]]

        PECA6 = [[(row-1, column-1), (row+1, column-1),
                  (row-2, column + 1), (row-2, column+3), (row+1, column+3)]]

        PECA7 = [[(row-1, column-1), (row+1, column-1), (row-2, column),
                  (row-2, column+2), (row-1, column+3), (row+1, column+3)]]

        PECA8 = [[(row-1, column-1), (row+1, column-1), (row-2, column),
                  (row-2, column+3), (row+1, column+2), (row, column+3)]]

        PECA9 = [[(row-2, column-1), (row+1, column-1),
                  (row-2, column+2), (row+1, column+2)]]

        PECA10 = [[(row-1, column-1), (row+1, column-1),
                   (row-1, column+5), (row+1, column+5)]]

        PECA11 = [[(row-1, column-1), (row+1, column-1),
                   (row-2, column+2), (row-2, column+4), (row+1, column+4)]]

        PECA12 = [[(row-1, column-1), (row+1, column-1), (row-2, column+1),
                   (row-2, column+3), (row-1, column+4), (row+1, column+4)]]

        PECA13 = [[(row-1, column-1), (row+1, column-1),
                   (row-2, column), (row-2, column+3), (row+1, column+3)]]

        PECA14 = [[(row-1, column-1), (row+1, column-1), (row-2, column+1),
                   (row-2, column+4), (row+1, column+3), (row, column+4)]]

        PECA15 = [[(row-1, column-1), (row+1, column-1),
                   (row-3, column+1), (row-3, column+3), (row+1, column+3)]]

        PECA16 = [[(row-1, column-1), (row+1, column-1), (row-3, column),
                   (row-3, column+3), (row-1, column+3), (row+1, column+2)]]

        PECA17 = [[(row-1, column-1), (row+1, column-1),
                   (row-3, column-1), (row-3, column+2), (row+1, column+2)]]

        PECA18 = [[(row-1, column-1), (row+1, column-1), (row-2, column),
                   (row-3, column+1), (row-3, column+3), (row, column+3), (row+1, column+2)]]

        PECA19 = [[(row-1, column-1), (row+1, column-1), (row-2, column), (row-2, column+2),
                   (row-1, column+3), (row+1, column+3), (row+2, column), (row+2, column+2)]]

        PECA20 = [[(row-1, column-1), (row+1, column-1),
                   (row-3, column), (row-3, column+2), (row+1, column+3), (row-1, column+3)]]

        PECA21 = [[(row-1, column-1), (row+1, column-1), (row-3, column),
                   (row-3, column+2), (row-2, column+3), (row, column+3), (row+1, column+2)]]

        return [PECA1, PECA2, PECA3, PECA4, PECA5, PECA6, PECA7, PECA8, PECA9, PECA10, PECA11, PECA12, PECA13, PECA14, PECA15, PECA16, PECA17, PECA18, PECA19, PECA20, PECA21]
    
    
    def roda_peca_esquerda(row, col, peca_selecionada):
        nova_peca = []
        for coord in peca_selecionada:
            x, y = coord
        # Rotaciona a peça em 90 graus
            nova_x = -y
            nova_y = x
            nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row, y - min_y + col) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca
    

    
    def roda_diagonais_esquerda(row, col, diagonais_peca):
        nova_peca = []
        for coord in diagonais_peca:
            x, y = coord
        # Rotaciona a peça em 90 graus
            nova_x = -y
            nova_y = x
            nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row-1, y - min_y + col-1) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca
    
    def roda_peca_direita(row, col, peca_selecionada):
        nova_peca = []
        for coord in peca_selecionada:
            x, y = coord
        # Rotaciona a peça em 90 graus
            nova_x = y
            nova_y = -x
            nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row, y - min_y + col) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca
    

    
    def roda_diagonais_direita(row, col, diagonais_peca):
        nova_peca = []
        for coord in diagonais_peca:
            x, y = coord
        # Rotaciona a peça em 90 graus
            nova_x = y
            nova_y = -x
            nova_peca.append((nova_x, nova_y))
    # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row-1, y - min_y + col-1) for x, y in nova_peca]
    # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca
    
    

    '''
    def roda_peca_esquerda(row, col, peca_selecionada):
        nova_peca = []
        for coord in peca_selecionada:
            x, y = coord
            # Rotaciona a peça em 90 graus
            nova_x = -y
            nova_y = x
            nova_peca.append((nova_x, nova_y))
        # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x, y - min_y) for x, y in nova_peca]
        # Desloca a peça para que a coordenada (0, 0) seja a primeira coordenada da peça inicial
        desloc_x = peca_selecionada[0][0] - nova_peca[0][0]
        desloc_y = peca_selecionada[0][1] - nova_peca[0][1]
        nova_peca = [(x + desloc_x, y + desloc_y) for x, y in nova_peca]
        # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca

    '''

    '''
    def roda_diagonais_esquerda(row, col, diagonais_peca):
        nova_peca = []
        for coord in diagonais_peca:
            x, y = coord
            # Rotaciona a peça em 90 graus no sentido contrário
            nova_x = -y
            nova_y = x
            nova_peca.append((nova_x, nova_y))
        # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row-1, y - min_y + col-1)
                     for x, y in nova_peca]
        # Ordena a lista de coordenadas para que a ordem seja consistente
        nova_peca = sorted(nova_peca)
        return nova_peca
    '''
    
    '''
    def roda_peca_direita(row, col, peca_selecionada):
        nova_peca = []
        for coord in peca_selecionada:
            x, y = coord
            # Rotaciona a peça em 90 graus
            nova_x = y
            nova_y = -x
            nova_peca.append((nova_x, nova_y))
        # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x, y - min_y) for x, y in nova_peca]
        # Desloca a peça para que a coordenada (0, 0) seja a primeira coordenada da peça inicial
        desloc_x = peca_selecionada[0][0] - nova_peca[0][0]
        desloc_y = peca_selecionada[0][1] - nova_peca[0][1]
        nova_peca = [(x + desloc_x, y + desloc_y) for x, y in nova_peca]
        # Ordena a lista de coordenadas para que a ordem seja consistente
        #nova_peca = sorted(nova_peca)
        return nova_peca

    def roda_diagonais_direita(row, col, diagonais_peca):
        nova_peca = []
        for coord in diagonais_peca:
            x, y = coord
            # Rotaciona a peça em 90 graus no sentido contrário
            nova_x = y
            nova_y = -x
            nova_peca.append((nova_x, nova_y))
        # Translada a peça para que sua coordenada superior esquerda seja (0, 0)
        min_x = min(x for x, y in nova_peca)
        min_y = min(y for x, y in nova_peca)
        nova_peca = [(x - min_x + row-1, y - min_y + col-1)
                     for x, y in nova_peca]
        # Ordena a lista de coordenadas para que a ordem seja consistente
        nova_peca = sorted(nova_peca)
        return nova_peca

    '''
