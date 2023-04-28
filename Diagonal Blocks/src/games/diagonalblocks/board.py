EMPTY_CELL = -1
PLAYANLE_CELL = 0
CONNECTING_CELL = 1

class Board:

    @staticmethod
    def get_all():
        try:
            Board.__all_pieces
        except AttributeError:
            _ = EMPTY_CELL
            o = CONNECTING_CELL
            X = PLAYANLE_CELL
            
            Board.__all_pieces = [
                    Board([
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
                    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]      
                    ])    
            ]

        return Board.__all_pieces

    def __init__(self, cfg):
        self.__cfg = cfg


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
    
    def is_valid_move(self, pieces, row, col):
        if self.board[row][col] != EMPTY_CELL:
            print("Posição já ocupada!")
            return False
        if pieces == []:
            print("Sem peças para colocar!")
            return False
        return True
    
    def draw_piece(self, place_piece, row, col):
        self.board[row][col] = place_piece
    
    """
    def is_valid_move(board, place_piece, row, col):
    # Verifica se as coordenadas estão dentro dos limites do tabuleiro
        if row < 0 or row >= board or col < 0 or col >= board[0]:
            return False

    # Verifica se a posição escolhida está vazia
        if board[row][col] != EMPTY_CELL:
            return False

    # Verifica se a peça pode ser colocada na posição escolhida
        for i in range(place_piece):
            for j in range(pieces):
                if pieces[i][j] != EMPTY_CELL:
                     if row + i >= board or col + j >= board[0] or board[row+i][col+j] != EMPTY_CELL:
                        return False

    # Se as coordenadas são válidas e a peça pode ser colocada ali, retorna True
        return True


    def draw_piece(place_piece, row, col):
        piece_height = place_piece
        piece_width = place_piece[0]

        # Verifica se é possível colocar a peça nas coordenadas especificadas
        for i in range(piece_height):
            for j in range(piece_width):
                if place_piece[i][j] != EMPTY_CELL:
                    new_row = row + i
                    new_col = col + j
                    if not (0 <= new_row < piece_height and 0 <= new_col < piece_width):
                        return False
                    if [new_row][new_col] != EMPTY_CELL:
                        return False

        # Atualiza o estado do tabuleiro para incluir a nova peça
        for i in range(piece_height):
            for j in range(piece_width):
                if place_piece[i][j] != EMPTY_CELL:
                    new_row = row + i
                    new_col = col + j
                    [new_row][new_col] = place_piece[i][j]

                    return True

                     """


