import pygame
from games.diagonalblocks.players.defensivegreedy import DefensiveGreedyPlayer
from games.diagonalblocks.players.minimax import OffensiveMinimaxPlayer
from games.diagonalblocks.players.defensiveminimax import DefensiveMinimaxPlayer
from games.diagonalblocks.players.human import HumanDiagonalBlocksPlayer
from games.diagonalblocks.players.offensivegreedy import OffensiveGreedyPlayer
from games.diagonalblocks.players.random import RandomDiagonalBlocksPlayer
from games.diagonalblocks.simulator import DiagonalBlocksSimulator
from games.game_simulator import GameSimulator
from games.diagonalblocks.piece import Piece
from games.diagonalblocks.board import Board
from games.diagonalblocks.piece import Piece

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

        print("Results for the game:")
        simulator.print_stats()


def main():
    print("Diagonal Blocks")


    num_iterations = 1

    diagonalblocks_simulations = [
        {
            "name": "TicTacToe - Human VS Human",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": HumanDiagonalBlocksPlayer("Human")
        },
        {
            "name": "TicTacToe - Human VS Random",
            "player1": HumanDiagonalBlocksPlayer("Human"),
            "player2": DefensiveMinimaxPlayer("Minimax")
        },
        {
            "name": "TicTacToe - Random VS Random",
            "player1": RandomDiagonalBlocksPlayer("Random 1"),
            "player2": RandomDiagonalBlocksPlayer("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": OffensiveGreedyPlayer("Greedy"),
            "player2": RandomDiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": OffensiveMinimaxPlayer("Minimax"),
            "player2": RandomDiagonalBlocksPlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": DefensiveMinimaxPlayer("Minimax"),
            "player2": DefensiveGreedyPlayer("Greedy")
        }
    ]

    for sim in diagonalblocks_simulations:
        run_simulation(sim["name"], DiagonalBlocksSimulator(sim["player1"], sim["player2"], 20), num_iterations)

def print_all_pieces(pieces):
        pieces = Piece.get_all()
        for piece in pieces:
            piece.print()
            #print("")

def select_piece(pieces):
        num_peca = int(input("Escolha uma peça: "))
        return pieces[num_peca - 1]

def select_row(pieces):
        x = int(input("Escolha uma linha: ")) 
        return x 

def select_column(pieces):
    y = int(input("Escolha uma coluna: "))
    return y
    
     

def get_user_choice():
        print("Opções:")
        print("1 - Selecionar peça")
        print("2 - Virar horizontalmente")
        print("3 - Virar verticalmente")
        print("4 - Rodar 90º")
        return int(input("Escolha uma opção: "))




if __name__ == "__main__":
    #main()


    places = Board.get_all()
    for place in places:
        place.print()

    pieces = Piece.get_all()
    print_all_pieces(pieces)
    place_piece = select_piece(pieces)
    x = select_row(pieces)
    y = select_column(pieces)
    print("Peça selecionada:")
    place_piece.print()

    #Board.print()


  
    """
    
    while moves_left > 0:
        print(f"Jogador {current_player}, é a sua vez!")
        Board.get_all()
        
        valid_input = False
        while not valid_input:
            coordinates = input("Digite as coordenadas para colocar a peça (no formato linha,coluna): ")
            coordinates = coordinates.split(",")
            row, col = int(coordinates[0]), int(coordinates[1])
            if Board.is_valid_move(place_piece, row, col):
                Board.draw_piece(place_piece, row, col)
                player1_pieces.remove_piece(place_piece)
                valid_input = True
        
            if current_player == 1:
                player1_pieces = pieces.get_all()    

            if current_player == 2:
                player2_pieces = pieces.get_all()         
        
            moves_left -= 1
        
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
            
    print("Fim de jogo!")

    """
    while True:
        opcao = get_user_choice()
        if opcao == 1:
            #place_piece = select_piece(pieces)
            print("Peça selecionada:")
            place_piece.print()
            break
        elif opcao == 2:
            place_piece.flip_hor()
        elif opcao == 3:
            place_piece.flip_ver()
        elif opcao == 4:
            place_piece.rotate90()
        
        print("Peça atual:")
        place_piece.print()
    
    
    def create_board():
        board = []
        for i in range(20):
            row = []
            for j in range(21):
                if i == 0:
                    if j == 0:
                        row.append(" ")
                    else:
                       
                        row.append(f"{j:2}")
                        
                elif j == 0:
                    row.append(f"{i:2} ")   
                    #row.append(f"{chr(i+64):2}")
                else:
                    row.append("  ")
            board.append(row)
        return board

board = create_board()

for row in board:
    
    print("□".join(row))

    
   
    
    
    
    

    '''
    pieces = Peca.get_all()


    for piece in pieces: 
        piece.print()
        print("")
        piece.flip_hor()
        piece.print()
        print("")
        piece.flip_ver()
        piece.print()
        
        print("")
        piece.rotate90()
        piece.print()
        print("")
    '''


