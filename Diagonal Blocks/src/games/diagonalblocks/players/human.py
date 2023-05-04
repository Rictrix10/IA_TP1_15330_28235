from games.diagonalblocks.action import DiagonalBlocksAction
from games.diagonalblocks.player import DiagonalBlocksPlayer
from games.diagonalblocks.state import DiagonalBlocksState
from games.diagonalblocks.piece import Piece


class HumanDiagonalBlocksPlayer(DiagonalBlocksPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DiagonalBlocksState):
        state.display()
        
        while True:
            # noinspection PyBroadException
            try:
                pieces = Piece.get_all()
                for pecas1 in pieces:
                    pecas1.print()
                
                
                row = (int(input(f"Player {state.get_acting_player()}, choose a row: ")))
                column = (int(input(f"Player {state.get_acting_player()}, choose a column: ")))
                piece = (int(input(f"Player {state.get_acting_player()}, choose a piece: ")))
                place_piece = pieces[piece]
                print("Peça selecionada:")
                place_piece.print()
                while True:
                    print("Escolha uma opção: \n 1 - Confirmar peça selecionada\n 2 - Rodar peça para a direita\n 3 - Rodar peça para a esquerda\n")
                    option = (int(input(f"Player {state.get_acting_player()}, choose a option: ")))
                    if option == 1:
                        break
                    elif option == 2:
                        place_piece.rotate_direita()
                    elif option == 3:
                        place_piece.rotate_esquerda()

                    print("Peça atual:")
                    place_piece.print()


                return DiagonalBlocksAction(row, column, piece, option)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: DiagonalBlocksState):
        # ignore
        pass

    def event_end_game(self, final_state: DiagonalBlocksState):
        # ignore
        pass
