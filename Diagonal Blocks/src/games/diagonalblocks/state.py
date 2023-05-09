import itertools
from typing import Optional

from games.diagonalblocks.action import DiagonalBlocksAction
from games.diagonalblocks.result import DiagonalBlocksResult
from games.state import State
from games.diagonalblocks.piece import Piece
game_pieces=[
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','■'],
    [' ','0',' ','■',' ',' ','1',' ','■','■',' ',' ','2',' ','■','■','■',' ',' ','3',' ','■','■',' ',' ','4',' ','■','■','■','■',' ',' ','5',' ','■','■','■',' ',' ',' ','6',' ','■','■','■',' ',' ','7',' ','■','■',' ',' ',' ','8',' ',' ','■','■',' ',' ','9',' ','■','■','■','■','■',' ',' ','1','0',' ','■','■','■','■'],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ','■','■'' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ',' ','■',' '],
    [' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ','■'' ',' ',' ',' ',' ',' ','■','■',' ',' ',' ',' ',' ','■','■','■',' ',' ',' ',' ',' ',' ','■',' ',' ',' ',' ',' ',' ',' ','■','■'],
    ['1','1',' ','■','■','■','■',' ',' ','1','2',' ','■','■','■',' ',' ','1','3',' ','■','■','■',' ',' ',' ','1','4',' ','■','■','■',' ',' ','1','5',' ','■','■',' ',' ','1','6',' ','■','■'' ',' ','1','7',' ','■','■',' ',' ',' ','1','8',' ',' ','■',' ',' ',' ','1','9',' ','■','■','■',' ',' ','2','0',' ','■','■','\n'],

]

class DiagonalBlocksState(State):
    EMPTY_CELL = -1
    DOT_CELLR = -2
    DOT_CELLB = -3
    DOT_CELLRB = -4
    


    def __init__(self, size: int = 20):
        super().__init__()

        if size < 20:
            raise Exception("the number of rows must be 20")

        """
        the dimensions of the board
        """
        self.size = size
        self.num_rows = size
        self.num_cols = size

        """
        the grid
        """
        
        self.grid = [[DiagonalBlocksState.EMPTY_CELL for _i in range(self.num_cols)] for _j in range(self.num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        #the index of the current acting player
        self.__acting_player = 0

        #determine if a winner was found already 
        self.__has_winner = False

        self.__total_pieces = 42

        self.__resultP0 = 0

        self.__resultP1 = 0

        self.__pieceNorepeatP0 = []

        self.__pieceNorepeatP1 = []

        self.__pecasP0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.__pecasP1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.__possible_movesP0 = []

        self.__possible_movesP1 = []



    def __check_winner(self, action: DiagonalBlocksAction) -> bool:
        return False

    def get_grid(self):
        return self.grid

    def get_num_players(self):
        return 2
    
    
    def __save_diagonais(self):
        diagonais = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.__acting_player == 0:
                    if self.grid[row][col] == DiagonalBlocksState.DOT_CELLR or self.grid[row][col] == DiagonalBlocksState.DOT_CELLRB:
                        diagonais.append((row,col))
                else:
                    if self.grid[row][col] == DiagonalBlocksState.DOT_CELLB or self.grid[row][col] == DiagonalBlocksState.DOT_CELLRB:
                        diagonais.append((row,col))
        return diagonais
    
    def validate_action(self, action: DiagonalBlocksAction) -> int:
        row = action.get_row()
        col = action.get_col()
        piece = action.get_piece()
        option = action.get_option()
        peca_selecionada = action.get_peca()

        all_actions = []        
       
        pecas_disponiveis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        linha: int
        coluna: int
        diagonais = self.__save_diagonais()
        
        for x in range(len(pecas_disponiveis)):
        #for x in range(len(self.__pecasP0)):
                for y in range(self.num_rows):
                    for z in range(self.num_cols):             
                            problema = 0
                            n = pecas_disponiveis[x]
                            #n = self.__pecasP0[x]
                            peca = Piece.criar_peca(y, z)
                            peca_escolhida = peca[n][0]

                            if self.__acting_player == 0:
                                if n not in self.__pecasP0:
                                    problema += 1
                            else:
                                if n not in self.__pecasP1:
                                    problema += 1
                            
                            if self.__turns_count > 2:
                                linha = peca_escolhida[0][0]
                                coluna = peca_escolhida[0][1]
                                if (linha,coluna) not in diagonais:
                                    problema += 1

                            
                            for b in range(len(peca_escolhida)):
                                linha = peca_escolhida[b][0]
                                coluna = peca_escolhida[b][1]
                                if linha < 0 or linha >= self.num_rows:
                                    problema += 1
                                if coluna < 0 or coluna >= self.num_cols:
                                    problema += 1
                            if problema == 0:
                                all_actions.append([n, y, z])
                                #self.__possible_movesP0.append([n, y, z])
                            
        #print("Jogadas que eram possíveis neste turno :", all_actions)                 

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # valid piece
        if piece < 0 or piece > 20:
            #return False
            return 0
        
        # valid column
        if col < 0 or col >= self.num_cols:
            #return False
            return 0
        
        # valid row
        if row < 0 or row >= self.num_rows:
            #return False
            return 0
        
        # free pieces
        erro = 0
        for x in range(len(peca_selecionada)):
            row = peca_selecionada[x][0]
            col = peca_selecionada[x][1] 
            if self.grid[row][col] == 0 or self.grid[row][col] == 1:
                erro += 1
        if erro > 0:
            print("Não pode jogar aí, peças não se podem sobrepor")
            #return False
            return 0
        
        # non-repeating play
        if self.__acting_player == 0:
            if piece not in self.__pecasP0:
                print("Essa peça já foi jogada, jogue outra")
                print(self.__pecasP0)
                #return False
                return 0
        else:
            if piece not in self.__pecasP1:
                print("Essa peça já foi jogada, jogue outra")
                print(self.__pecasP1)
                #return False 
                return 0

        # play in diagonal
        coordenadas = self.__save_diagonais()

        encontrou = 0
        if self.__turns_count > 2:
            row = peca_selecionada[0][0]
            col = peca_selecionada[0][1]
            if (row,col) in coordenadas:
                encontrou += 1
            if encontrou == 0:
                print("Não pode jogar aí, tem que jogar numa diagonal de uma das suas peças")
                print(coordenadas)
                #return False
                return 0
            #return True
        
        #play in board
        
        saiu = 0
        for x in range(len(peca_selecionada)):
            row = peca_selecionada[x][0]
            col = peca_selecionada[x][1]
            if row < 0 or row >= self.num_rows:
                saiu += 1
            if col < 0 or col >= self.num_cols:
                saiu += 1
        if saiu > 0:
            print("Não pode jogar aí, a peça tem de ser jogada dentro da tabuleiro")
            #return False
        
        if self.__acting_player == 0:
            if len(all_actions) == 0 and self.__pecasP0 != 0:
            #if len(all_actions) == 0:
                return 2
        else:
            if len(all_actions) == 0 and self.__pecasP1 != 0:
            #if len(all_actions) == 0:
                return 2
        #self.possible_actions()
        
        #return True
        return 1


    def update(self, action: DiagonalBlocksAction):
        col = action.get_col()
        row = action.get_row()
        piece = action.get_piece()
        peca_selecionada = action.get_peca()
        diagonais_selecionadas = action.get_diagonais()

        print()
        
        for x in range(len(peca_selecionada)):
            row = peca_selecionada[x][0]
            col = peca_selecionada[x][1]
            self.grid[row][col] = self.__acting_player

        if  self.__acting_player == 0:
            self.__resultP0 += len(peca_selecionada)
            self.__pieceNorepeatP0.append(piece)
            #self.__pecasP0.remove(piece)
            self.__pecasP0.remove(action.get_piece())                         
        
        if self.__acting_player == 1:
            self.__resultP1 += len(peca_selecionada)
            self.__pieceNorepeatP1.append(piece)
            #self.__pecasP1.remove(piece) 
            self.__pecasP1.remove(action.get_piece())
        print("\n\t\t\tTurno", self.__turns_count, " - Player 0 [",  self.__resultP0, "-", self.__resultP1, "] Player 1\n")

        for x in range(len(diagonais_selecionadas)):
            row = diagonais_selecionadas[x][0]
            col = diagonais_selecionadas[x][1]
            if self.__acting_player == 0:
                if self.grid[row][col] == DiagonalBlocksState.DOT_CELLR or self.grid[row][col] == DiagonalBlocksState.EMPTY_CELL:
                    self.grid[row][col] = DiagonalBlocksState.DOT_CELLR

                if self.grid[row][col] == DiagonalBlocksState.DOT_CELLB:
                    self.grid[row][col] = DiagonalBlocksState.DOT_CELLRB
            else:
                if self.grid[row][col] == DiagonalBlocksState.DOT_CELLB or self.grid[row][col] == DiagonalBlocksState.EMPTY_CELL:
                    self.grid[row][col] = DiagonalBlocksState.DOT_CELLB

                if self.grid[row][col] == DiagonalBlocksState.DOT_CELLR:
                   self.grid[row][col] = DiagonalBlocksState.DOT_CELLRB
        # determine if there is a winner
        
        self.__has_winner = self.__check_winner(action)
        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0
        self.__turns_count += 1

    

    
    def possible_actions(self) -> list:
 
        jogadas = []
        #pecas_disponiveis = []
        diagonais = self.__save_diagonais()
        
        
        if self.__acting_player == 0:
            pecas_disponiveis = list(self.__pecasP0)
            #pecas_disponiveis = self.__pecasP0

        else :
            pecas_disponiveis = list(self.__pecasP1)
            #pecas_disponiveis = self.__pecasP1
           
        #pecas_disponiveis = self.pecas_disponiveis()

        
        for x in range(len(pecas_disponiveis)):
        #for x in range(len(self.__pecasP0)):
                for y in range(self.num_rows):
                    for z in range(self.num_cols):             
                            erro = 0
                            n = pecas_disponiveis[x]
                            #n = self.__pecasP0[x]
                            peca = Piece.criar_peca(y, z)
                            peca_selecionada = peca[n][0]
                            
                            if self.__turns_count > 2:
                                row = peca_selecionada[0][0]
                                col = peca_selecionada[0][1]
                                if (row,col) not in diagonais:
                                    erro += 1

                            
                            for b in range(len(peca_selecionada)):
                                row = peca_selecionada[b][0]
                                col = peca_selecionada[b][1]
                                if row < 0 or row >= self.num_rows:
                                    erro += 1
                                if col < 0 or col >= self.num_cols:
                                    erro += 1
                            if erro == 0:
                                jogadas.append([n, y, z])
                                #self.__possible_movesP0.append([n, y, z])
                            
                           
        return jogadas
        #return self.__possible_movesP0
    
            

    def __display_cell(self, row, col):
            print({
                0: '\033[91m▩\033[0m',   
                1: '\033[96m▩\033[0m',   
                DiagonalBlocksState.EMPTY_CELL: ' ',
                DiagonalBlocksState.DOT_CELLR: '\033[91m▫\033[0m',
                DiagonalBlocksState.DOT_CELLB: '\033[96m▫\033[0m',     
                DiagonalBlocksState.DOT_CELLRB: '\033[95m▫\033[0m'
            }[self.grid[row][col]], end="")
    
    def __display_numbers(self):
        # exibir números das colunas
            max_digits = len(str(self.num_cols-1))
            for col in range(0, self.num_cols):
                if col == 0:
                    print(' '*(2+max_digits-1), end="")
                if col < 20:
                    if col < 10:
                        print(' '*(max_digits-1), end=" ")
                    else: 
                        print(''*(max_digits-2), end=" ")
                print(col, end=" ")
            print("")     

    def __display_separator(self):
            for col in range(0, self.num_cols):
                print("----", end="") 
            print("--")
                
    def display(self):
            self.__display_numbers()
                # exibir números das linhas e células
            for row in range(self.num_rows):
                print('', end=" ")
                print('{:<2d}'.format(row), end=" ")
                for col in range(self.num_cols):
                    self.__display_cell(row, col)
                    print(' | ', end="")
                print("")
                self.__display_separator()

            self.__display_numbers()
            print("")

            for i in game_pieces:
                for j in i:
                    print(j, end="")
                print()
            
    
    def __is_full(self):
        
        return self.__turns_count > self.__total_pieces
    


    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DiagonalBlocksState(self.num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cloned_state.grid[row][col] = self.grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DiagonalBlocksResult]:
        if self.__has_winner:
            return DiagonalBlocksResult.WIN if pos == self.__acting_player else DiagonalBlocksResult.LOOSE
        if self.__is_full():
            return DiagonalBlocksResult.DRAW
        return None

    def get_num_rows(self):
        return self.num_rows

    def get_num_cols(self):
        return self.num_cols

    def before_results(self):
        pass


    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state


    