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
                    print("", end="")
                elif place == PLAYANLE_CELL:
                    print("▮", end="")
                else:
                    raise ValueError("Invalid piece definition")
            print("")

            Board = [[0] * 20 for _ in range(20)]
    
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
    
   

   

    